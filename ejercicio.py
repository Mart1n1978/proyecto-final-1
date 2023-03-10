import sqlite3

conexion = sqlite3.connect('base.sqlite')
cursor = conexion.cursor()


cursor.execute("PRAGMA foreign_keys = ON")  # Activación de claves foráneas para Sqlite
conexion.commit()  # Guarda cambios

def crear_tablas():
    cursor.execute("""
        CREATE TABLE Pais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    
    print("Tabla creada")
    cursor.execute("""
        CREATE TABLE Producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
            )
    """)

    print("Tabla creada")
    cursor.execute("""
        CREATE TABLE Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            nacimiento TEXT,
            pais_origen_id REFERENCES Pais(id) ON DELETE SET NULL
            )
    """)

    print("Tabla creada")

    cursor.execute("""
        CREATE TABLE Cliente_Producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id REFERENCES Cliente(id) ON DELETE CASCADE,
            producto_id REFERENCES Producto(id) ON DELETE CASCADE
            )
    """)

    print("Tabla creada")

def pais_agregar():
    try:
        cursor.execute("INSERT INTO Pais (nombre) VALUES (?)", ("Argentina",))
        conexion.commit()
    except Exception as e:
        print("error", e)
    else:
        print('Paises creados')

def pais_agregar_2():
    paises = ["Brasil", "Chile", "México", "Ecuador", "Colombia", "Uruguay"]

    for pais in paises:
        cursor.execute("INSERT INTO Pais (nombre) VALUES (?)", (pais,))
    conexion.commit() #esto es para grabar a la base de datos y no dejar los datos en la memoria

print("Paises creados")

# crear_tablas()
# pais_agregar()
