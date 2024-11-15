import re
from .usql_dictionary import sql_to_usql as SQL_TO_USQL

def sql_to_usql(query):
    """
    Traduce una consulta SQL a USQL.
    
    Args:
        query (str): La consulta en SQL.
    
    Returns:
        str: La consulta traducida a USQL.
    
    Raises:
        ValueError: Si la consulta no es válida.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("La consulta SQL no puede estar vacía o ser de un tipo no válido.")

    # Tokenizar la consulta SQL utilizando palabras y símbolos clave
    tokens = re.findall(r'\w+|\S', query)
    translated_tokens = []

    # Traducción de SQL a USQL utilizando el diccionario de palabras clave
    for token in tokens:
        translated_token = SQL_TO_USQL.get(token.upper(), token)
        translated_tokens.append(translated_token)

    # Unir los tokens traducidos para formar la consulta en USQL
    usql_query = ' '.join(translated_tokens).strip()

    # Limpiar espacios innecesarios
    usql_query = re.sub(r'\s+', ' ', usql_query)  # Reemplazar múltiples espacios por uno solo
    usql_query = re.sub(r'\bDE LA TABLA\b', 'DE_LA_TABLA', usql_query)  # Reemplazar "DE LA TABLA" por "DE_LA_TABLA"
    usql_query = re.sub(r'\s*=\s*', ' = ', usql_query)  # Espacios alrededor de '='
    usql_query = re.sub(r"\s*'\s*", "'", usql_query)  # Quitar espacios antes y después de "'"

    # Asegurar que todas las partes clave están correctamente espaciadas
    usql_query = re.sub(r'\s*(LOS VALORES|DONDE|SETEA)\s*', r' \1 ', usql_query)

    # Eliminar cualquier espacio antes del punto y coma
    usql_query = re.sub(r'\s*;\s*$', ';', usql_query)

    # Validar si la traducción es plausible
    if not usql_query.endswith(';'):
        raise ValueError("La consulta traducida no parece válida. Debe terminar con ';'.")

    return usql_query
