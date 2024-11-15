# usql_parser.py

import ply.yacc as yacc
from .usql_lexer import tokens  # Asegúrate de importar el lexer con los tokens ya definidos
from .usql_dictionary import sql_to_usql_mapping  # Diccionario para traducción

# Regla de inicio
def p_query(t):
    '''query : select_query
             | insert_query
             | update_query
             | delete_query
             | alter_query'''
    t[0] = t[1]

# Reglas de SELECT
def p_select_query(t):
    '''select_query : TRAEME TODO DE_LA_TABLA table_name DONDE condition
                    | TRAEME LOS_DISTINTOS column_name DE_LA_TABLA table_name DONDE condition
                    | TRAEME CONTANDO LPAREN TODO RPAREN DE_LA_TABLA table_name AGRUPANDO_POR column_name HAVING condition'''

    if len(t) == 7:  # Caso SELECT *
        t[0] = f"SELECT * FROM {t[4]} WHERE {t[6]}"
    elif len(t) == 8:  # Caso SELECT DISTINCT
        t[0] = f"SELECT DISTINCT {t[3]} FROM {t[5]} WHERE {t[7]}"
    elif len(t) == 12:  # Caso SELECT COUNT con ajuste
        t[0] = f"SELECT COUNT(*) FROM {t[7]} GROUP BY {t[9]} HAVING {t[11]}"





# Reglas de INSERT
def p_insert_query(t):
    '''insert_query : METE_EN table_name LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPAREN'''
    t[0] = f"INSERT INTO {t[2]} ({t[4]}) VALUES ({t[8]})"

# Reglas de UPDATE
def p_update_query(t):
    '''update_query : ACTUALIZA table_name SETEA column_name EQUAL value DONDE condition'''
    t[0] = f"UPDATE {t[2]} SET {t[4]} = {t[6]} WHERE {t[8]}"

def p_delete_query(t):
    '''delete_query : BORRA_DE_LA table_name DONDE condition'''
    if len(t) == 5:
        t[0] = f"DELETE FROM {t[2]} WHERE {t[4]}"


# Reglas de ALTER TABLE
def p_alter_query(t):
    '''alter_query : CAMBIA_LA_TABLA table_name AGREGA_LA_COLUMNA column_name data_type NO_NULO
                   | CAMBIA_LA_TABLA table_name ELIMINA_LA_COLUMNA column_name'''
    if len(t) == 7:
        t[0] = f"ALTER TABLE {t[2]} ADD COLUMN {t[4]} {t[5]} NOT NULL"
    else:
        t[0] = f"ALTER TABLE {t[2]} DROP COLUMN {t[4]}"

# Reglas auxiliares para nombres de tablas y columnas
def p_table_name(t):
    'table_name : ID'
    t[0] = t[1]

def p_column_name(t):
    'column_name : ID'
    t[0] = t[1]

# Reglas para listas de columnas y valores
def p_column_list(t):
    'column_list : column_name COMMA column_list'
    t[0] = f"{t[1]}, {t[3]}"

def p_column_list_single(t):
    'column_list : column_name'
    t[0] = t[1]

def p_value_list(t):
    'value_list : value COMMA value_list'
    t[0] = f"{t[1]}, {t[3]}"

def p_value_list_single(t):
    'value_list : value'
    t[0] = t[1]

# Valores permitidos
def p_value(t):
    '''value : STRING
             | NUMBER'''
    if isinstance(t[1], str):
        t[0] = f"'{t[1]}'"
    else:
        t[0] = t[1]

# Reglas para condiciones y expresiones
def p_condition(t):
    '''condition : expression
                 | expression AND condition'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = f"{t[1]} AND {t[3]}"

def p_expression(t):
    '''expression : column_name EQUAL value
                  | column_name GREATER value
                  | column_name LESS value
                  | column_name ENTRE value AND value
                  | column_name LIKE value'''
    if t[2] == "ENTRE":
        t[0] = f"{t[1]} BETWEEN {t[3]} AND {t[5]}"
    else:
        t[0] = f"{t[1]} {t[2]} {t[3]}"

# Definir tipos de datos
def p_data_type(t):
    '''data_type : INTEGER
                 | VARCHAR
                 | FLOAT'''
    t[0] = t[1]

# Manejo de errores de sintaxis
def p_error(t):
    if t:
        print(f"Error de sintaxis en '{t.value}'")
        raise SyntaxError(f"Error de sintaxis en '{t.value}'")
    else:
        print("Error de sintaxis al final del input")
        raise SyntaxError("Error de sintaxis al final del input")

# Construcción del parser
parser = yacc.yacc(debug=True)

# Función para parsear consultas USQL
def parse_usql(query):
    result = parser.parse(query)
    return result


# Función para parsear consultas SQL a USQL
def parse_sql(sql_query):
    for sql_word, usql_word in sql_to_usql_mapping.items():
        sql_query = sql_query.replace(sql_word, usql_word)
    return sql_query
