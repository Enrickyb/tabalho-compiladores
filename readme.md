# Trabalho Prático de Compiladores: Analisador Léxico

Este repositório contém o código-fonte de um analisador léxico desenvolvido para a disciplina de Compiladores.

## [cite_start]Descrição da Linguagem "Simples"

A linguagem "Simples" é uma linguagem de programação procedural e didática, criada para este trabalho. Ela suporta variáveis, operações aritméticas e relacionais, e estruturas de controle básicas.

### [cite_start]Especificação dos Tokens

Os tokens da linguagem são definidos pelas seguintes expressões regulares:

- **Identificadores**: `[a-zA-Z][a-zA-Z0-9]*`
  - _Exemplo_: `variavel`, `soma1`, `resultado`
- **Palavras-Chave**: `programa`, `inteiro`, `real`, `leia`, `escreva`, `se`, `senao`, `enquanto`, `faca`
- **Operadores Aritméticos**: `+`, `-`, `*`, `/`
- **Operadores Relacionais**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Atribuição**: `=`
- **Delimitadores**: `(`, `)`, `{`, `}`, `;`, `,`
- **Números Inteiros**: `[0-9]+`
  - _Exemplo_: `10`, `42`
- **Números de Ponto Flutuante**: `[0-9]+\.[0-9]+`
  - _Exemplo_: `3.14`, `99.9`

## [cite_start]Instruções para Compilação e Execução

O analisador léxico foi desenvolvido em Python e não requer compilação.

### Requisitos

- Python 3.x

### Execução

Para executar o analisador, utilize o seguinte comando no terminal, passando como argumento o caminho para um arquivo de código-fonte escrito na linguagem "Simples":

```bash
python analisador_lexico.py programa_exemplo.txt
```

O programa irá imprimir a lista de tokens reconhecidos no formato `(TIPO_DO_TOKEN, LEXEMA)`. Em caso de erro léxico, uma mensagem será exibida no erro padrão.

## [cite_start]Demonstração com Programa de Exemplo

**Arquivo `programa_exemplo.txt`:**

```
programa {
    inteiro a;
    a = 10;
    se (a > 5) {
        escreva a;
    }
}
```

**Saída da Execução:**

```
('PALAVRA_CHAVE', 'programa')
('DELIM', '{')
('PALAVRA_CHAVE', 'inteiro')
('ID', 'a')
('DELIM', ';')
('ID', 'a')
('ATRIBUICAO', '=')
('NUM_INTEIRO', '10')
('DELIM', ';')
('PALAVRA_CHAVE', 'se')
('DELIM', '(')
('ID', 'a')
('OP_REL', '>')
('NUM_INTEIRO', '5')
('DELIM', ')')
('DELIM', '{')
('PALAVRA_CHAVE', 'escreva')
('ID', 'a')
('DELIM', ';')
('DELIM', '}')
('DELIM', '}')
```
