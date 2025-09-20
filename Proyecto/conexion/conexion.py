import mysql.connector
from mysql.connector import errorcode

config = {
    "host": "localhost",
    "user": "root",
    "password": "12345",  # reemplaza con tu contraseña
    "database": "desarrollo_web"
}

try:
    db = mysql.connector.connect(**config)
    print("Conexión exitosa a 'desarrollo_web'!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos 'desarrollo_web' no existe. Creándola...")
        try:
            db = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"]
            )
            cursor = db.cursor()
            cursor.execute("CREATE DATABASE desarrollo_web")
            print("Base de datos 'desarrollo_web' creada exitosamente!")
            db.database = "desarrollo_web"
        except mysql.connector.Error as err2:
            print("Error al crear la base de datos:", err2)
    else:
        print("X Error al conectar:", err)

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Conexión cerrada.")