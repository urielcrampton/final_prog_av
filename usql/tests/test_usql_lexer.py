# test_usql_lexer.py
import unittest
from usql.src.usql_lexer import lexer

class TestUSQLLexer(unittest.TestCase):
    
    def test_select_query(self):
        query = "TRAEME TODO DE_LA_TABLA estudiantes DONDE edad ENTRE 18 AND 25"
        lexer.input(query)
        tokens = [(token.type, token.value) for token in lexer]
        expected_tokens = [
            ('TRAEME', 'TRAEME'),
            ('TODO', 'TODO'),
            ('DE_LA_TABLA', 'DE_LA_TABLA'),
            ('ID', 'estudiantes'),
            ('DONDE', 'DONDE'),
            ('ID', 'edad'),
            ('ENTRE', 'ENTRE'),
            ('NUMBER', 18),
            ('AND', 'AND'),
            ('NUMBER', 25)
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_insert_query(self):
        query = "METE_EN estudiantes (nombre, edad) LOS_VALORES ('Juan', 20)"
        lexer.input(query)
        tokens = [(token.type, token.value) for token in lexer]
        expected_tokens = [
            ('METE_EN', 'METE_EN'),
            ('ID', 'estudiantes'),
            ('LPAREN', '('),
            ('ID', 'nombre'),
            ('COMMA', ','),
            ('ID', 'edad'),
            ('RPAREN', ')'),
            ('LOS_VALORES', 'LOS_VALORES'),
            ('LPAREN', '('),
            ('STRING', 'Juan'),
            ('COMMA', ','),
            ('NUMBER', 20),
            ('RPAREN', ')')
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_update_query(self):
        query = "ACTUALIZA estudiantes SETEA edad EQUAL 21 DONDE nombre LIKE 'Juan%'"
        lexer.input(query)
        tokens = [(token.type, token.value) for token in lexer]
        expected_tokens = [
            ('ACTUALIZA', 'ACTUALIZA'),
            ('ID', 'estudiantes'),
            ('SETEA', 'SETEA'),
            ('ID', 'edad'),
            ('EQUAL', 'EQUAL'),
            ('NUMBER', 21),
            ('DONDE', 'DONDE'),
            ('ID', 'nombre'),
            ('LIKE', 'LIKE'),
            ('STRING', 'Juan%')
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_delete_query(self):
        query = "BORRA_DE_LA estudiantes DONDE edad MENOR 18"
        lexer.input(query)
        tokens = [(token.type, token.value) for token in lexer]
        expected_tokens = [
            ('BORRA_DE_LA', 'BORRA_DE_LA'),
            ('ID', 'estudiantes'),
            ('DONDE', 'DONDE'),
            ('ID', 'edad'),
            ('ID', 'MENOR'),
            ('NUMBER', 18)
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_alter_query(self):
        query = "CAMBIA_LA_TABLA estudiantes AGREGA_LA_COLUMNA direccion VARCHAR NO_NULO"
        lexer.input(query)
        tokens = [(token.type, token.value) for token in lexer]
        expected_tokens = [
            ('CAMBIA_LA_TABLA', 'CAMBIA_LA_TABLA'),
            ('ID', 'estudiantes'),
            ('AGREGA_LA_COLUMNA', 'AGREGA_LA_COLUMNA'),
            ('ID', 'direccion'),
            ('VARCHAR', 'VARCHAR'),
            ('NO_NULO', 'NO_NULO')
        ]
        self.assertEqual(tokens, expected_tokens)

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()