# Plataforma do Minicurso · Genômica Clínica

Página estática de apoio ao minicurso **Interpretação Clínica de Variantes Genômicas Germinativas: Aplicação dos Critérios ACMG em Dados de Sequenciamento de Exoma**.

Pensada para hospedagem em **GitHub Pages** e reutilizável em diferentes edições do curso.

## Como hospedar no GitHub

1. Crie um novo repositório público no GitHub (ex.: `minicurso-genomica-clinica`).
2. Faça upload do arquivo `index.html` e das pastas de materiais na raiz do repositório.
3. Ative o GitHub Pages: **Settings → Pages → Source: Deploy from a branch → Branch: `main` / folder: `/root`**.
4. Após alguns minutos, sua página estará em `https://SEU-USUARIO.github.io/minicurso-genomica-clinica/`.

## Estrutura de pastas recomendada

```
/
├── index.html                 ← página principal
├── materiais/                 ← slides e handouts em PDF
│   ├── mod01_slides.pdf
│   ├── mod01_handout.pdf
│   ├── mod02_slides.pdf
│   ├── mod02_criterios.pdf
│   ├── mod03_slides.pdf
│   ├── mod03_calibracao.pdf
│   ├── mod04_slides.pdf
│   └── mod04_casos.pdf
├── dados/                     ← VCFs, workflows Galaxy, planilhas
│   ├── caso01.vcf.gz
│   ├── caso02.vcf.gz
│   ├── caso03.vcf.gz
│   ├── galaxy_workflow_wes.ga
│   ├── galaxy_workflow_panel.ga
│   └── planilha_acmg.xlsx
└── artigos/                   ← PDFs de artigos científicos
    ├── richards_2015.pdf
    ├── tavtigian_2018.pdf
    ├── abou_tayoun_2018.pdf
    ├── pejaver_2022.pdf
    └── chen_2024.pdf
```

## Personalização

Toda configuração fica em um único bloco no topo do `<script>` no `index.html`, marcado como `CONFIGURAÇÃO`.

### E-mails autorizados

```js
const AUTHORIZED_EMAILS = [
  'chaves.smo@gmail.com',
  'aluno1@exemplo.com',
  'aluno2@ufsc.br',
];
```

### Aceitar domínios acadêmicos automaticamente

```js
const ACCEPT_ACADEMIC_DOMAINS = true;  // aceita .edu.br, ufsc.br, etc.
```

### Link do Google Meet

```js
const MEET_LINK = 'https://meet.google.com/abc-defg-hij';
```

### Conteúdo

Cada seção tem seu próprio array: `MODULES`, `DATA_FILES`, `VIDEOS`, `ARTICLES`, `LINKS`, `SCHEDULE`. Edite seguindo o modelo de cada item.

Para vídeos, use o link embed do YouTube (`https://www.youtube.com/embed/ID_DO_VIDEO`).

## Segurança

Este é um sistema de controle de acesso client-side. Qualquer pessoa suficientemente técnica pode inspecionar o código-fonte e ver a lista de e-mails autorizados. Aceitável para materiais acadêmicos de curso, mas não use para dados sensíveis.

## Tecnologias

- HTML/CSS/JS puro
- Tailwind CSS via CDN
- Lucide Icons via CDN
- Google Fonts (Instrument Serif, Inter, JetBrains Mono)
- Sem build, sem dependências, sem servidor
