# Plataforma do Minicurso · Interpretação Clínica de Variantes Genômicas

Ambiente de apoio ao minicurso **Interpretação Clínica de Variantes Genômicas Germinativas: Aplicação dos Critérios ACMG em Dados de Sequenciamento de Exoma**, do I SIMOL 2026.

Aqui ficam reunidos, em um só lugar, o link da sala, a ementa, os materiais teóricos, os artigos de referência, os arquivos de dados dos casos e os vídeos-tutorial. A plataforma foi desenvolvida para acompanhar os dois encontros do minicurso e é reaproveitável em edições futuras.

---

## Acesso

O acesso é restrito aos inscritos. Entre com o e-mail que você informou na inscrição, o mesmo em que recebeu as orientações do minicurso.

Reconheça o ambiente com antecedência. Durante as aulas você vai navegar por ele enquanto acompanha a prática, então vale entrar antes do primeiro encontro e ver onde está cada coisa.

---

## O que você encontra aqui

- **Sala do minicurso** — o link do Google Meet, o mesmo nos dois dias.
- **Ementa** — objetivo, conteúdo, metodologia e pré-requisitos.
- **Materiais** — slides, apostilas e handouts de cada módulo.
- **Dados** — os arquivos VCF dos casos, o VCF de exemplo e o workflow do Galaxy.
- **Artigos** — as referências que embasam os critérios trabalhados no curso.
- **Vídeos** — tutoriais de apoio às plataformas.
- **Enquetes** — o questionário de nivelamento (antes do curso) e o de feedback (ao final).

---

## Antes do primeiro encontro

Três coisas precisam estar prontas antes de terça:

1. **Conta no Franklin by Genoox** — https://franklin.genoox.com
2. **Conta no Galaxy** — https://usegalaxy.org
3. **Questionário de nivelamento respondido** — na aba Enquetes, cerca de 8 minutos.

As duas contas são gratuitas. Use o e-mail da sua instituição, se você tiver um, porque é por ele que o Franklin libera o acesso acadêmico.

Baixe também, com antecedência, o VCF de exemplo e os arquivos dos casos. São arquivos grandes, e deixar o download para o início da aula custa tempo de todos.

Sem as duas contas criadas não é possível acompanhar a parte prática, que ocupa metade da carga horária.

---

## O percurso

No primeiro encontro, começamos subindo os arquivos nas plataformas, já que o processamento demora e precisa ficar pronto para o segundo dia. Em seguida, percorremos o caminho do FASTQ ao VCF anotado no Galaxy e passamos aos critérios ACMG/AMP com os refinamentos do ClinGen.

No segundo encontro, o Franklin na prática: upload, filtros, painéis virtuais e classificação de variantes em casos reais.

Não é exigida experiência prévia com bioinformática.

---

## Sobre o acesso restrito

O controle de acesso funciona no próprio navegador e serve para organizar a turma, não para proteger dados sensíveis. Os materiais aqui são de uso didático. Nenhum dado de paciente real identificável é disponibilizado na plataforma.

---

## Suporte

Problemas de acesso à plataforma ou às contas do Franklin e do Galaxy devem ser resolvidos antes do primeiro encontro. Em caso de dificuldade, entre em contato com o ministrante com antecedência.

**Dr. Tiago Fernando Chaves** — LAPOGE/CCB/UFSC

---

<details>
<summary>Nota técnica (manutenção)</summary>

Página estática em HTML, CSS e JavaScript, sem build e sem servidor, hospedada em GitHub Pages. Toda a configuração (e-mails autorizados, link do Meet, materiais, cronograma) fica em um único bloco marcado como `CONFIGURAÇÃO`, no topo do `<script>` em `index.html`. As seções de conteúdo são arrays editáveis: `MODULES`, `DATA_FILES`, `VIDEOS`, `ARTICLES`, `LINKS`, `POLLS` e `SCHEDULE`. Recursos externos (Tailwind, Lucide, Google Fonts) são carregados via CDN.

</details>
