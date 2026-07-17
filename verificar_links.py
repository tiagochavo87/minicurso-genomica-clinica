#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador de links do site do minicurso.

Confere cada arquivo declarado no index.html contra:
  1. a existência no disco
  2. o rastreamento pelo git (arquivo ignorado nunca chega ao GitHub Pages)
  3. os limites de tamanho do GitHub (aviso em 50 MB, bloqueio em 100 MB)
  4. o tamanho declarado no site versus o tamanho real

USO
---
    cd X:\\minicurso-genomica-clinica
    python verificar_links.py

Sem dependências externas. Python 3.6+.
"""

import io
import os
import re
import subprocess
import sys
from urllib.parse import unquote

RAIZ = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(RAIZ, 'index.html')

AVISO_GITHUB = 50 * 1024 * 1024    # GitHub avisa
BLOQUEIO_GITHUB = 100 * 1024 * 1024  # GitHub recusa o push

VERDE, VERM, AMAR, AZUL, RESET = '\033[92m', '\033[91m', '\033[93m', '\033[94m', '\033[0m'
if os.name == 'nt' and not os.environ.get('WT_SESSION'):
    VERDE = VERM = AMAR = AZUL = RESET = ''


def humano(n):
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024:
            return '%.0f %s' % (n, u) if u == 'B' else '%.1f %s' % (n, u)
        n /= 1024.0
    return '%.1f TB' % n


def git(*args):
    try:
        r = subprocess.run(['git'] + list(args), cwd=RAIZ,
                           capture_output=True, text=True, timeout=30)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def main():
    if not os.path.isfile(HTML):
        print(VERM + 'index.html não encontrado em %s' % RAIZ + RESET)
        return 1

    html = io.open(HTML, encoding='utf-8').read()

    # Todos os campos file: '...' e url: '...'
    alvos = re.findall(r"file:\s*'([^']+)'", html)
    alvos += re.findall(r"url:\s*'([^']+)'", html)

    # Tamanhos declarados, para conferir se o site está descrevendo versão antiga
    declarados = dict(re.findall(r"file:\s*'([^']+)',\s*size:\s*'([^']+)'", html))

    rastreados = git('ls-files')
    tem_git = rastreados is not None
    rastreados = set(rastreados.split('\n')) if tem_git else set()

    locais = [a for a in alvos if not a.startswith(('http://', 'https://', 'mailto:', '#'))]
    externos = [a for a in alvos if a.startswith(('http://', 'https://'))]

    print(AZUL + '=' * 74)
    print('VERIFICAÇÃO DE LINKS · site do minicurso')
    print('=' * 74 + RESET)
    print('Raiz : %s' % RAIZ)
    print('Git  : %s' % ('sim' if tem_git else 'não detectado'))
    print('Alvos: %d locais, %d externos\n' % (len(locais), len(externos)))

    problemas, avisos = [], []

    print(AZUL + '--- ARQUIVOS LOCAIS ' + '-' * 54 + RESET)
    for alvo in locais:
        rel = unquote(alvo)
        caminho = os.path.join(RAIZ, rel.replace('/', os.sep))
        nome = rel.split('/')[-1]

        if not os.path.isfile(caminho):
            print(VERM + '  [404]  %s' % nome + RESET)
            print('         declarado: %s' % rel)
            problemas.append('Arquivo não existe: %s' % rel)
            continue

        tam = os.path.getsize(caminho)
        obs = []

        # git
        if tem_git:
            posix = rel.replace(os.sep, '/')
            if posix not in rastreados:
                obs.append(VERM + 'NÃO RASTREADO PELO GIT' + RESET)
                problemas.append('Fora do git (não vai para o Pages): %s' % rel)

        # tamanho
        if tam >= BLOQUEIO_GITHUB:
            obs.append(VERM + 'EXCEDE 100 MB, GITHUB BLOQUEIA' + RESET)
            problemas.append('Acima de 100 MB: %s (%s)' % (rel, humano(tam)))
        elif tam >= AVISO_GITHUB:
            obs.append(AMAR + 'acima de 50 MB, GitHub avisa' + RESET)
            avisos.append('Grande: %s (%s)' % (rel, humano(tam)))

        # tamanho declarado versus real
        if alvo in declarados:
            d = declarados[alvo]
            num = re.match(r'([\d.]+)\s*(B|KB|MB|GB)', d, re.I)
            if num:
                mult = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}[num.group(2).upper()]
                esperado = float(num.group(1)) * mult
                if esperado > 0 and abs(tam - esperado) / esperado > 0.20:
                    obs.append(AMAR + 'site diz %s, real %s' % (d, humano(tam)) + RESET)
                    avisos.append('Tamanho desatualizado: %s (site: %s, real: %s)'
                                  % (rel, d, humano(tam)))

        marca = VERDE + '  [ok] ' + RESET if not obs else AMAR + '  [!!] ' + RESET
        print('%s %-52s %9s' % (marca, nome[:52], humano(tam)))
        for o in obs:
            print('         %s' % o)

    # Arquivos no disco que o site não referencia
    print('\n' + AZUL + '--- ÓRFÃOS (no disco, fora do site) ' + '-' * 38 + RESET)
    refs = set(unquote(a).replace('/', os.sep) for a in locais)
    achou = False
    for pasta in ('materiais', 'dados', 'artigos'):
        base = os.path.join(RAIZ, pasta)
        if not os.path.isdir(base):
            continue
        for dirp, _, arqs in os.walk(base):
            for a in arqs:
                if a.startswith('.') or a.endswith(('.py', '.txt')):
                    continue
                rel = os.path.relpath(os.path.join(dirp, a), RAIZ)
                if rel not in refs:
                    print(AMAR + '  [órfão] %s' % rel + RESET)
                    achou = True
    if not achou:
        print('  nenhum')

    # .gitignore
    print('\n' + AZUL + '--- .gitignore ' + '-' * 59 + RESET)
    for dirp, _, arqs in os.walk(RAIZ):
        if '.git' + os.sep in dirp + os.sep:
            continue
        if '.gitignore' in arqs:
            cam = os.path.join(dirp, '.gitignore')
            print(AMAR + '  %s' % os.path.relpath(cam, RAIZ) + RESET)
            for ln in io.open(cam, encoding='utf-8', errors='replace'):
                ln = ln.strip()
                if ln and not ln.startswith('#'):
                    print('      %s' % ln)

    # Resumo
    print('\n' + AZUL + '=' * 74)
    print('RESUMO')
    print('=' * 74 + RESET)
    if problemas:
        print(VERM + '%d PROBLEMA(S) QUE QUEBRAM O SITE:' % len(problemas) + RESET)
        for p in problemas:
            print('  · %s' % p)
    else:
        print(VERDE + 'Nenhum problema crítico.' + RESET)

    if avisos:
        print(AMAR + '\n%d aviso(s):' % len(avisos) + RESET)
        for a in avisos:
            print('  · %s' % a)

    print('\n' + AZUL + 'Links externos declarados (confira manualmente):' + RESET)
    for e in sorted(set(externos)):
        if 'COLE_AQUI' in e:
            print(VERM + '  [PLACEHOLDER NÃO PREENCHIDO] %s' % e + RESET)
        else:
            print('  %s' % e)

    return 1 if problemas else 0


if __name__ == '__main__':
    sys.exit(main())
