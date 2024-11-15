#fluent_api.py
class USQLQuery:
    def __init__(self):
        self.query = ""

    def traeme(self, fields):
        self.query += f"TRAEME {fields} "
        return self

    def de_la_tabla(self, table):
        self.query += f"DE LA TABLA {table} "
        return self

    def donde(self, condition):
        self.query += f"DONDE {condition} "
        return self

    def agrupar_por(self, field):
        self.query += f"AGRUPANDO POR {field} "
        return self

    def mezclar(self, table, condition):
        self.query += f"MEZCLANDO {table} EN {condition} "
        return self

    def los_distintos(self, fields):
        self.query = self.query.replace("TRAEME", "TRAEME LOS DISTINTOS", 1)
        self.query += f"{fields} "
        return self

    def contando(self, fields):
        self.query += f"TRAEME CONTANDO({fields}) "
        return self

    def mete_en(self, table, fields):
        self.query = f"METE EN {table} ({fields}) "
        return self

    def los_valores(self, values):
        self.query += f"LOS VALORES ({values}) "
        return self

    def actualiza(self, table):
        self.query = f"ACTUALIZA {table} "
        return self

    def setea(self, condition):
        self.query += f"SETEA {condition} "
        return self

    def borra_de_la(self, table):
        self.query = f"BORRA DE LA {table} "
        return self

    def como_mucho(self, limit):
        self.query += f"CÓMO MUCHO {limit} "
        return self

    def where_del_group_by(self, condition):
        self.query += f"HAVING {condition} "
        return self

    def entre(self, start, end):
        self.query += f"ENTRE {start} Y {end} "
        return self

    def build(self):
        return self.query.strip() + ";"



