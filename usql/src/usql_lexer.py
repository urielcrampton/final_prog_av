# usql_lexer.py
import ply.lex as lex
from .usql_dictionary import sql_to_usql, usql_to_sql_mapping, sql_to_usql_mapping

# Definimos la lista de tokens en base a las claves del diccionario
tokens = [key.replace(" ", "_").replace("(", "").replace(")", "") for key in sql_to_usql.keys() if key != "*"]

# Agregamos tokens específicos para "*", identificadores, números, operadores y símbolos adicionales
tokens.extend([
    'ASTERISK', 'ID', 'NUMBER', 'GREATER', 'GREATER_EQUAL', 'LESS', 'LESS_EQUAL', 'EQUAL', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'COMMA', 'AND', 'LOS_DISTINTOS', 'AGRUPANDO_POR', 'BORRA_DE_LA', 'CAMBIA_LA_TABLA',
    'AGREGA_LA_COLUMNA', 'ELIMINA_LA_COLUMNA', 'NO_NULO', 'STRING'
])

# Tokens adicionales específicos de USQL
tokens.extend(['TRAEME', 'TODO', 'DE_LA_TABLA', 'DONDE', 'CONTANDO', 'METE_EN', 'LOS_VALORES', 'ACTUALIZA', 'SETEA'])

# Expresiones regulares para los nuevos tokens
t_TRAEME = r'TRAEME'
t_TODO = r'TODO'
t_DE_LA_TABLA = r'DE_LA_TABLA'
t_DONDE = r'DONDE'
t_CONTANDO = r'CONTANDO'
t_METE_EN = r'METE_EN'
t_LOS_VALORES = r'LOS_VALORES'
t_ACTUALIZA = r'ACTUALIZA'
t_SETEA = r'SETEA'

# En usql_lexer.py
tokens.extend(['INTEGER', 'VARCHAR', 'FLOAT'])  # Asegúrate de incluir los tipos de datos necesarios

# Define patrones para los tipos de datos
t_INTEGER = r'INTEGER'
t_VARCHAR = r'VARCHAR'
t_FLOAT = r'FLOAT'


# Expresiones regulares para tokens adicionales de SQL-USQL
t_LOS_DISTINTOS = r'LOS_DISTINTOS'
t_AGRUPANDO_POR = r'AGRUPANDO_POR'
t_BORRA_DE_LA = r'BORRA_DE_LA'
t_CAMBIA_LA_TABLA = r'CAMBIA_LA_TABLA'
t_AGREGA_LA_COLUMNA = r'AGREGA_LA_COLUMNA'
t_ELIMINA_LA_COLUMNA = r'ELIMINA_LA_COLUMNA'
t_NO_NULO = r'NO_NULO'

# Definimos los patrones de los tokens basados en el diccionario, excepto "*"
for key in sql_to_usql.keys():
    token_name = key.replace(" ", "_").replace("(", "").replace(")", "")
    if key != "*":  # Excluir "*"
        globals()[f't_{token_name}'] = r'\b' + key + r'\b'

# Definir patrones específicos para los tokens
t_ASTERISK = r'\*'
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_LESS = r'<'
t_LESS_EQUAL = r'<='
t_EQUAL = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_AND = r'AND'

tokens.extend(['ENTRE'])
t_ENTRE = r'ENTRE'



# Ignoramos espacios y tabulaciones
t_ignore = ' \t'

# Definimos cómo manejar identificadores (ID)

# Definimos cómo manejar números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convertir el valor a número entero
    return t

# Definimos cómo manejar cadenas de texto (si se requieren)
def t_STRING(t):
    r'\'([^\\\']|\\.)*\'|"([^\\\"]|\\.)*"'  # Permitir tanto comillas simples como dobles
    t.value = t.value[1:-1]  # Eliminar las comillas
    return t


# Definimos cómo manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definimos cómo manejar errores léxicos
def t_error(t):
    
    print(f"Carácter no válido: '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Definir el manejo del fin de archivo
def t_eof(t):
    return None


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Si el valor coincide con alguno de los tokens definidos, se asigna como tipo de token.
    if t.value.upper() in tokens:  
        t.type = t.value.upper()
    return t


# Construir el lexer
lexer = lex.lex()


