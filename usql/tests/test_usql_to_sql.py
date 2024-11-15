# test_usql_to_sql.py
import unittest
from usql.src.usql_to_sql import usql_to_sql

class TestUSQLToSQL(unittest.TestCase):

    def test_simple_select(self):
        usql_query = "TRAEME TODO DE LA TABLA usuarios;"
        expected_sql = "SELECT * FROM usuarios;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_select_with_condition(self):
        usql_query = "TRAEME nombre DE LA TABLA usuarios DONDE edad > 18;"
        expected_sql = "SELECT nombre FROM usuarios WHERE edad > 18;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_insert_statement(self):
        usql_query = "METE EN usuarios (nombre, edad) LOS VALORES ('Agustin', 25);"
        expected_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Agustin', 25);"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_update_statement(self):
        usql_query = "ACTUALIZA usuarios SETEA edad = 26 DONDE nombre = 'Agustin';"
        expected_sql = "UPDATE usuarios SET edad = 26 WHERE nombre = 'Agustin';"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_delete_statement(self):
        usql_query = "BORRA DE LA usuarios DONDE edad < 20;"
        expected_sql = "DELETE FROM usuarios WHERE edad < 20;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_invalid_usql_syntax(self):
        usql_query = "TRAEME TODO DONDE edad > 18;"  # Falta DE LA TABLA
        with self.assertRaises(ValueError):
            usql_to_sql(usql_query)

    def test_empty_query(self):
        usql_query = ""
        with self.assertRaises(ValueError):
            usql_to_sql(usql_query)

    def test_missing_semicolon(self):
        usql_query = "TRAEME TODO DE LA TABLA usuarios"
        with self.assertRaises(ValueError):
            usql_to_sql(usql_query)

if __name__ == '__main__':
    unittest.main()
