# Documentador Automático de Código

## Motivação

Na faculdade, frequentemente precisamos documentar códigos em nossos trabalhos e projetos. Esse processo pode ser repetitivo e consumir bastante tempo, principalmente quando os códigos são extensos.

A ideia deste projeto surgiu para **automatizar a geração de documentação** de funções e classes em código Python, facilitando a vida do desenvolvedor e permitindo que ele se concentre mais na lógica do programa do que na escrita manual de README ou comentários detalhados.

## Como a solução foi construída

O projeto utiliza Python para analisar o código enviado pelo usuário e gerar automaticamente um README.md com a seguinte estrutura:

- Detecção de **funções** e **classes** usando o módulo `ast` (Abstract Syntax Tree).
- Geração de descrições detalhadas para cada função e classe utilizando **OpenAI**, garantindo documentação compreensível e informativa.
- Montagem automática de um arquivo `README.md` contendo todas as funções, classes e suas descrições geradas.

A arquitetura é simples: o usuário fornece um arquivo `.py`, o script processa o código, chama a API do OpenAI para gerar explicações e salva tudo em um README.md organizado.

## Instruções para rodar

1. **Clonar o repositório**:

```bash
git clone https://github.com/pedropaffaro/Documenter.git
cd Documenter
```

2. **Instalar dependências**:

```bash
pip install -r requirements.txt
```

## Próximos passos

- Adicionar suporte a outras linguagens, além do Python.
- Melhorar a formatação do README, incluindo exemplos de uso e diagramas de classes.
- Permitir a atualização incremental da documentação, sem sobrescrever o README existente.
- Criar uma interface web simples para upload de códigos e geração automática de documentação.
