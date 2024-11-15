import unittest
from usql.src.usql_parser import parse_usql

class TestUSQLParser(unittest.TestCase):

    def test_select_query_basic(self):
        query = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 30"
        expected_output = "SELECT * FROM usuarios WHERE edad > 30"
        self.assertEqual(parse_usql(query), expected_output)

    def test_select_query_distinct(self):
        query = "TRAEME LOS_DISTINTOS nombre DE_LA_TABLA usuarios DONDE ciudad = 'Montevideo'"
        expected_output = "SELECT DISTINCT nombre FROM usuarios WHERE ciudad = 'Montevideo'"
        self.assertEqual(parse_usql(query), expected_output)

    def test_select_query_count(self):
        query = "TRAEME CONTANDO ( TODO ) DE_LA_TABLA ventas AGRUPANDO_POR vendedor HAVING total > 1000"
        expected_output = "SELECT COUNT(*) FROM ventas GROUP BY vendedor HAVING total > 1000"
        self.assertEqual(parse_usql(query), expected_output)

    def test_insert_query(self):
        query = "METE_EN usuarios (nombre, edad, ciudad) LOS_VALORES ('Agustin', 25, 'Montevideo')"
        expected_output = "INSERT INTO usuarios (nombre, edad, ciudad) VALUES ('Agustin', 25, 'Montevideo')"
        self.assertEqual(parse_usql(query), expected_output)

    def test_update_query(self):
        query = "ACTUALIZA usuarios SETEA edad = 26 DONDE nombre ='Agustin'"
        expected_output = "UPDATE usuarios SET edad = 26 WHERE nombre = 'Agustin'"
        self.assertEqual(parse_usql(query), expected_output)

    def test_delete_query(self):
        query = "BORRA_DE_LA usuarios DONDE edad < 20"
        expected_output = "DELETE FROM usuarios WHERE edad < 20"
        self.assertEqual(parse_usql(query), expected_output)

    def test_alter_query_add_column(self):
        query = "CAMBIA_LA_TABLA usuarios AGREGA_LA_COLUMNA email VARCHAR NO_NULO"
        expected_output = "ALTER TABLE usuarios ADD COLUMN email VARCHAR NOT NULL"
        self.assertEqual(parse_usql(query), expected_output)

    def test_alter_query_drop_column(self):
        query = "CAMBIA_LA_TABLA usuarios ELIMINA_LA_COLUMNA email"
        expected_output = "ALTER TABLE usuarios DROP COLUMN email"
        self.assertEqual(parse_usql(query), expected_output)

    def test_invalid_query(self):
        query = "TRAEME usuarios SIN_DONDE edad > 30"
        with self.assertRaises(SyntaxError):
            parse_usql(query)

if __name__ == '__main__':
    unittest.main()
