import os
from datetime import datetime

def formatar_tamanho(tamanho_bytes):
    """Formata o tamanho em bytes para uma unidade legível (KB, MB, GB)."""
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if tamanho_bytes < 1024.0:
            return f"{tamanho_bytes:.2f} {unidade}"
        tamanho_bytes /= 1024.0
    return f"{tamanho_bytes:.2f} TB"

def gerar_mapeamento_completo(pasta_alvo, arquivo_saida="mapeamento_estrutura.txt"):
    if not os.path.exists(pasta_alvo):
        print(f"Erro: A pasta '{pasta_alvo}' não existe. Verifique o caminho.")
        return

    linhas = []
    linhas.append("=" * 90)
    linhas.append("RELATÓRIO DE MAPEAMENTO COMPLETO DE DIRETÓRIOS E ARQUIVOS")
    linhas.append(f"Diretório Raiz: {os.path.abspath(pasta_alvo)}")
    linhas.append(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    linhas.append("=" * 90 + "\n")

    contagem_extensoes = {}
    total_arquivos = 0
    total_pastas = 0
    tamanho_total = 0

    # Varre a pasta recursivamente usando os.walk
    for raiz, pastas, arquivos in os.walk(pasta_alvo):
        # Ignora pastas ocultas normais (opcional)
        # pastas[:] = [d for d in pastas if not d.startswith('.')]
        
        caminho_relativo = os.path.relpath(raiz, pasta_alvo)
        nome_pasta = "📁 Raiz (./)" if caminho_relativo == "." else f"📁 {caminho_relativo}"
        
        # Nível de indentação visual para a estrutura de pastas
        nivel = caminho_relativo.count(os.sep) if caminho_relativo != "." else 0
        indentacao = "  " * nivel
        
        linhas.append(f"{indentacao}{nome_pasta}")
        linhas.append(f"{indentacao}" + "-" * (60 - len(indentacao)))
        total_pastas += 1

        if not arquivos:
            linhas.append(f"{indentacao}  [Pasta vazia ou sem arquivos diretos]")
            linhas.append("")
            continue

        for arq in arquivos:
            caminho_completo = os.path.join(raiz, arq)
            try:
                estatisticas = os.stat(caminho_completo)
                tamanho = estatisticas.st_size
                tamanho_str = formatar_tamanho(tamanho)
                modificado = datetime.fromtimestamp(estatisticas.st_mtime).strftime('%d/%m/%Y %H:%M')
                
                # Coleta extensão
                _, extensao = os.path.splitext(arq)
                extensao = extensao.lower() if extensao else "[Sem extensão]"
                contagem_extensoes[extensao] = contagem_extensoes.get(extensao, 0) + 1
                
                total_arquivos += 1
                tamanho_total += tamanho
                
                # Adiciona arquivo ao relatório com detalhes de metadados gerais
                linhas.append(f"{indentacao}  ├── {arq}")
                linhas.append(f"{indentacao}  │   └── Tipo: {extensao.upper().replace('.', '')} | Tam: {tamanho_str} | Modificado: {modificado}")
            except Exception as e:
                linhas.append(f"{indentacao}  ├── {arq} [Erro ao ler metadados: {str(e)}]")
        
        linhas.append("") # Espaço em branco entre seções

    # Seção de estatísticas resumidas ao final do arquivo
    linhas.append("=" * 90)
    linhas.append("RESUMO DA PASTA")
    linhas.append("=" * 90)
    linhas.append(f"Total de pastas mapeadas: {total_pastas - 1}") # subtrai 1 pois a raiz conta no os.walk
    linhas.append(f"Total de arquivos encontrados: {total_arquivos}")
    linhas.append(f"Tamanho total ocupado: {formatar_tamanho(tamanho_total)}")
    linhas.append("\nDistribuição por Extensão:")
    
    # Ordena as extensões por quantidade decrescente
    ext_ordenadas = sorted(contagem_extensoes.items(), key=lambda x: x[1], reverse=True)
    for ext, qtd in ext_ordenadas:
        linhas.append(f"  - {ext}: {qtd} arquivo(s)")
    linhas.append("=" * 90)

    # Escreve no TXT
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print(f"Mapeamento concluído com sucesso em '{arquivo_saida}'")

if __name__ == '__main__':
    # Modifique o caminho abaixo para a pasta desejada
    gerar_mapeamento_completo('./')
