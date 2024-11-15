import unittest
from usql.src.fluent_api import USQLQuery

class TestUSQLQuery(unittest.TestCase):

    def test_simple_select(self):
        query = USQLQuery().traeme("*").de_la_tabla("usuarios").build()
        expected = "TRAEME * DE LA TABLA usuarios;"
        self.assertEqual(query, expected)

    def test_select_with_condition(self):
        query = (USQLQuery()
                 .traeme("nombre")
                 .de_la_tabla("usuarios")
                 .donde("edad > 18")
                 .build())
        expected = "TRAEME nombre DE LA TABLA usuarios DONDE edad > 18;"
        self.assertEqual(query, expected)



    def test_counting(self):
        query = (USQLQuery()
                 .contando("id")
                 .de_la_tabla("usuarios")
                 .build())
        expected = "TRAEME CONTANDO(id) DE LA TABLA usuarios;"
        self.assertEqual(query, expected)

    def test_insert_statement(self):
        query = (USQLQuery()
                 .mete_en("usuarios", "nombre, edad")
                 .los_valores("'Agustin', 25")
                 .build())
        expected = "METE EN usuarios (nombre, edad) LOS VALORES ('Agustin', 25);"
        self.assertEqual(query, expected)

    def test_update_statement(self):
        query = (USQLQuery()
                 .actualiza("usuarios")
                 .setea("edad = 26")
                 .donde("nombre = 'Agustin'")
                 .build())
        expected = "ACTUALIZA usuarios SETEA edad = 26 DONDE nombre = 'Agustin';"
        self.assertEqual(query, expected)

    def test_delete_statement(self):
        query = (USQLQuery()
                 .borra_de_la("usuarios")
                 .donde("edad < 20")
                 .build())
        expected = "BORRA DE LA usuarios DONDE edad < 20;"
        self.assertEqual(query, expected)

    def test_group_by(self):
        query = (USQLQuery()
                 .traeme("nombre")
                 .de_la_tabla("usuarios")
                 .agrupar_por("edad")
                 .build())
        expected = "TRAEME nombre DE LA TABLA usuarios AGRUPANDO POR edad;"
        self.assertEqual(query, expected)

    def test_join(self):
        query = (USQLQuery()
                 .traeme("usuarios.nombre")
                 .de_la_tabla("usuarios")
                 .mezclar("pedidos", "usuarios.id = pedidos.usuario_id")
                 .build())
        expected = "TRAEME usuarios.nombre DE LA TABLA usuarios MEZCLANDO pedidos EN usuarios.id = pedidos.usuario_id;"
        self.assertEqual(query, expected)

    def test_limit(self):
        query = (USQLQuery()
                 .traeme("*")
                 .de_la_tabla("usuarios")
                 .como_mucho(10)
                 .build())
        expected = "TRAEME * DE LA TABLA usuarios CÓMO MUCHO 10;"
        self.assertEqual(query, expected)

    def test_having(self):
        query = (USQLQuery()
                 .traeme("edad")
                 .de_la_tabla("usuarios")
                 .agrupar_por("nombre")
                 .where_del_group_by("COUNT(*) > 1")
                 .build())
        expected = "TRAEME edad DE LA TABLA usuarios AGRUPANDO POR nombre HAVING COUNT(*) > 1;"
        self.assertEqual(query, expected)

    def test_between(self):
        query = (USQLQuery()
                 .traeme("nombre")
                 .de_la_tabla("usuarios")
                 .donde("edad ENTRE 20 Y 30")
                 .build())
        expected = "TRAEME nombre DE LA TABLA usuarios DONDE edad ENTRE 20 Y 30;"
        self.assertEqual(query, expected)

if __name__ == '__main__':
    unittest.main()
