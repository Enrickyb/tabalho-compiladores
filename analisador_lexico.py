import re
import sys

# Especificação dos Tokens com Expressões Regulares
# A ordem é importante: COMENTARIO vem antes de OP_ARIT
TOKEN_ESPECIFICACAO = [
    ('COMENTARIO',  r'//.*'),              # Comentário de linha única
    ('NUM_REAL',    r'\d+\.\d+'),          # Número de ponto flutuante
    ('NUM_INTEIRO', r'\d+'),               # Número inteiro
    ('ATRIBUICAO',  r'='),                 # Símbolo de atribuição
    ('ID',          r'[A-Za-z]\w*'),       # Identificadores
    ('OP_ARIT',     r'[+\-*/]'),           # Operadores Aritméticos
    ('OP_REL',      r'==|!=|<=|>=|<|>'),  # Operadores Relacionais
    ('DELIM',       r'[\(\)\{\};,]'),     # Delimitadores
    ('NOVA_LINHA',  r'\n'),                # Quebra de linha
    ('ESPACO',      r'[ \t]+'),            # Espaço em branco
    ('ERRO',        r'.'),                 # Qualquer outro caractere (erro)
]

# Compila as expressões regulares para eficiência
TOKEN_REGEX = re.compile('|'.join('(?P<%s>%s)' % pair for pair in TOKEN_ESPECIFICACAO))

# Palavras-Chave da Linguagem
PALAVRAS_CHAVE = {'programa', 'inteiro', 'real', 'leia', 'escreva', 'se', 'senao', 'enquanto', 'faca'}

def analisar_lexicamente(codigo_fonte):
    """
    Função principal que realiza a análise léxica.
    Recebe uma string com o código fonte e retorna uma lista de tokens.
    """
    tokens = []
    num_linha = 1
    for mo in TOKEN_REGEX.finditer(codigo_fonte):
        tipo_token = mo.lastgroup
        lexema = mo.group()

        if tipo_token == 'NOVA_LINHA':
            num_linha += 1
            continue
        elif tipo_token == 'ESPACO':
            continue # Ignora espaços em branco
        elif tipo_token == 'COMENTARIO':
            continue # Ignora comentários
        elif tipo_token == 'ID' and lexema in PALAVRAS_CHAVE:
            tipo_token = 'PALAVRA_CHAVE'
        elif tipo_token == 'ERRO':
            # Emite uma mensagem de erro clara e informativa
            sys.stderr.write(f'Erro léxico na linha {num_linha}: Caractere inesperado "{lexema}"\n')
            continue
        
        tokens.append((tipo_token, lexema))
        
    return tokens

if __name__ == '__main__':
    # Verifica se o nome do arquivo foi passado como argumento
    if len(sys.argv) != 2:
        print("Uso: python analisador_lexico.py <arquivo_fonte>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            codigo = arquivo.read()
            lista_tokens = analisar_lexicamente(codigo)
            for token in lista_tokens:
                print(token)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")