import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear la tabla 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
);
''')

# Crear la tabla 'clientes'
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    ciudad TEXT NOT NULL,
    edad INTEGER NOT NULL
);
''')

# Crear la tabla 'empleados'
cursor.execute('''
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    puesto TEXT NOT NULL,
    salario REAL NOT NULL
);
''')

# Crear la tabla 'pedidos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
''')

# Crear la tabla 'ventas'
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL
);
''')

# Insertar datos de ejemplo
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Pedro', 19);")
cursor.execute("INSERT INTO clientes (nombre, ciudad, edad) VALUES ('Maria', 'Madrid', 30);")
cursor.execute("INSERT INTO clientes (nombre, ciudad, edad) VALUES ('Lucas', 'Barcelona', 22);")
cursor.execute("INSERT INTO empleados (nombre, puesto, salario) VALUES ('Carlos', 'ingeniero', 2500);")
cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (1);")  # Asumiendo que el cliente con id=1 es Maria
cursor.execute("INSERT INTO ventas (producto, cantidad) VALUES ('Producto A', 10);")
cursor.execute("INSERT INTO ventas (producto, cantidad) VALUES ('Producto B', 6);")

# Guardar los cambios y cerrar la conexión
conn.commit()

# Ahora puedes hacer las consultas que mencionaste
# Ejemplo de consulta: TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;
cursor.execute("SELECT * FROM usuarios WHERE edad > 18;")
print("Usuarios mayores de 18:")
print(cursor.fetchall())

# Consulta: TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';
cursor.execute("SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';")
print("Clientes en Madrid:")
print(cursor.fetchall())

# Cerrar la conexión
conn.close()
