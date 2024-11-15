import re
from .usql_dictionary import sql_to_usql

# Diccionario inverso para traducir de USQL a SQL
USQL_TO_SQL = {v: k for k, v in sql_to_usql.items()}

# Función para convertir USQL a SQL
def usql_to_sql(usql_query):
    """
    Convierte una consulta USQL en una consulta SQL.
    
    :param usql_query: str, consulta en USQL
    :return: str, consulta en SQL
    :raises ValueError: si la consulta contiene sintaxis inválida o no reconocida
    """
    sql_query = usql_query

    # Primero, reemplazar las palabras clave compuestas
    for usql_keyword, sql_keyword in sorted(USQL_TO_SQL.items(), key=lambda x: len(x[0]), reverse=True):
        sql_query = re.sub(r'\b' + re.escape(usql_keyword) + r'\b', sql_keyword, sql_query)

    # Validar la consulta SQL resultante
    if not is_valid_sql(sql_query) or not sql_query.strip().endswith(";"):
        raise ValueError(f"Consulta USQL no válida: {usql_query}")
    
    return sql_query

# Función para validar una consulta SQL básica
def is_valid_sql(sql_query):
    """
    Verifica si una consulta SQL es válida.
    
    :param sql_query: str, consulta en SQL
    :return: bool, True si la consulta es válida, False en caso contrario
    """
    # Verificar que no esté vacía y termine en punto y coma
    if not sql_query.strip() or not sql_query.strip().endswith(";"):
        return False
    
    # Definir patrones para diferentes tipos de consultas
    select_pattern = r"^SELECT .+ FROM .+;"
    insert_pattern = r"^INSERT INTO .+ \(.+\) VALUES \(.+\);"
    update_pattern = r"^UPDATE .+ SET .+ WHERE .+;"
    delete_pattern = r"^DELETE FROM .+ WHERE .+;"
    
    # Validar la consulta con patrones
    if (re.match(select_pattern, sql_query) or
        re.match(insert_pattern, sql_query) or
        re.match(update_pattern, sql_query) or
        re.match(delete_pattern, sql_query)):
        return True
    
    return False