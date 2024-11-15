USQL_DSL_Project/
│
├── src/
│   ├── __init__.py          # Archivo inicializador del paquete, puede estar vacío o incluir metadatos sobre el paquete.
    ├── usql_dictionary.py        # Diccionario que contiene las traducciones de palabras clave
│   ├── usql_lexer.py        # Contiene el analizador léxico (lexer) utilizando PLY para definir tokens y reconocer palabras  
|                              clave de USQL y SQL.
│   ├── usql_parser.py       # Incluye el parser que define la gramática de USQL. Transforma consultas de USQL a SQL y viceversa.
│   ├── sql_to_usql.py       # Funciones para traducir consultas de SQL a USQL, manejando excepciones para consultas no válidas.
│   ├── usql_to_sql.py       # Funciones para traducir consultas de USQL a SQL, asegurando que la consulta resultante sea válida.
│   └── fluent_api.py        # Implementación del Fluent API en Python que permite encadenar consultas de manera programática.
│
├── tests/
│   ├── __init__.py          # Archivo inicializador para el paquete de tests, puede estar vacío o incluir metadatos.
│   ├── test_sql_to_usql.py  # Pruebas unitarias para verificar la correcta traducción de SQL a USQL.
│   ├── test_usql_to_sql.py  # Pruebas unitarias para verificar la correcta traducción de USQL a SQL.
│   ├── test_fluent_api.py   # Pruebas para asegurar que el Fluent API construya correctamente las consultas.
│   └── coverage_report.txt  # Reporte de cobertura de tests, indicando la cobertura lograda.
│
├── database/
│   ├── db_setup.sql         # Script SQL para crear las tablas necesarias para las pruebas del sistema.
│   └── db_teardown.sql      # Script SQL para eliminar las tablas después de las pruebas.
│
├── requirements.txt         # Lista de dependencias del proyecto, como PLY, pytest, y pycobertura.
├── pyproject.toml           # Archivo de configuración para gestionar el proyecto y las herramientas de análisis.
└── README.md                # Documentación del proyecto, incluye descripción, instalación y ejecución de pruebas.
----
python -m tests.test_usql_lexer
python -m tests.test_parser
python -m tests.test_sql_to_usql
python -m tests.test_usql_to_sql
