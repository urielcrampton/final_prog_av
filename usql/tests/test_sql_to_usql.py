# test_sql_to_usql.py
import unittest
from usql.src.sql_to_usql import sql_to_usql

class TestSQLToUSQL(unittest.TestCase):

    def test_simple_select(self):
        query = "SELECT * FROM usuarios;"
        expected_usql = "TRAEME TODO DE_LA_TABLA usuarios;"
        self.assertEqual(sql_to_usql(query), expected_usql)

    def test_select_with_condition(self):
        query = "SELECT nombre FROM usuarios WHERE edad > 18;"
        expected_usql = "TRAEME nombre DE_LA_TABLA usuarios DONDE edad > 18;"
        self.assertEqual(sql_to_usql(query), expected_usql)

    def test_insert_statement(self):
        query = "INSERT INTO usuarios (nombre, edad) VALUES ('Agustin', 25);"
        expected_usql = "INSERT INTO usuarios ( nombre , edad ) LOS VALORES ('Agustin', 25 );"
        self.assertEqual(sql_to_usql(query), expected_usql)

    def test_update_statement(self):
        query = "UPDATE usuarios SET edad = 26 WHERE nombre = 'Agustin';"
        expected_usql = "ACTUALIZA usuarios SETEA edad = 26 DONDE nombre ='Agustin';"
        self.assertEqual(sql_to_usql(query), expected_usql)

    def test_delete_statement(self):
        query = "DELETE FROM usuarios WHERE edad < 20;"
        expected_usql = "DELETE DE_LA_TABLA usuarios DONDE edad < 20;"
        self.assertEqual(sql_to_usql(query), expected_usql)

    def test_empty_query(self):
        with self.assertRaises(ValueError):
            sql_to_usql("")

    def test_invalid_query_type(self):
        with self.assertRaises(ValueError):
            sql_to_usql(None)

    def test_missing_semicolon(self):
        query = "SELECT * FROM usuarios"
        with self.assertRaises(ValueError):
            sql_to_usql(query)

if __name__ == '__main__':
    unittest.main()
