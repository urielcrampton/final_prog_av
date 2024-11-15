# __init__.py
__version__ = "0.1.0"

from .usql_lexer import tokens
from .usql_parser import parse_sql, parse_usql
from .sql_to_usql import sql_to_usql
from .usql_to_sql import usql_to_sql
from .fluent_api import USQLQuery
from .usql_lexer import lexer

"""
Paquete USQL DSL
----------------
Este paquete implementa el DSL USQL (Uruguayan Structured Query Language) para traducir consultas
entre USQL y SQL, y proporciona una API fluida para construir consultas USQL de manera programática.
"""
