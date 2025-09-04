import os
import json
import csv
from flask import Flask, render_template

app = Flask(__name__)

# Carpeta donde se guardarán los archivos de datos
CARPETA_DATOS = "datos"

# Asegurarse de que la carpeta exista
if not os.path.exists(CARPETA_DATOS):
    os.makedirs(CARPETA_DATOS)

# Lista de productos
productos = [
    {"id": "G001", "nombre": "Google Pixel 4", "cantidad": 10, "precio": 60.0, "imagen": "Google Pixel 4.jpg"},
    {"id": "G002", "nombre": "Google Pixel 6 Pro", "cantidad": 5, "precio": 95.0, "imagen": "Google Pixel 6 Pro.jpg"},
    {"id": "G003", "nombre": "Google Pixel 6", "cantidad": 7, "precio": 100.0, "imagen": "Google Pixel 6.jpg"},
    {"id": "G004", "nombre": "Google Pixel 7 Pro", "cantidad": 4, "precio": 95.0, "imagen": "Google Pixel 7 Pro.jpg"},
    {"id": "H001", "nombre": "Honor 10 Lite", "cantidad": 8, "precio": 40.0, "imagen": "Honor 10 Lite.jpg"},
    {"id": "H002", "nombre": "Honor 200 Lite", "cantidad": 6, "precio": 65.0, "imagen": "Honor 200 Lite.jpg"}
]

# ===== Funciones de persistencia =====
def guardar_txt(productos):
    with open(os.path.join(CARPETA_DATOS, "datos.txt"), "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['id']},{p['nombre']},{p['cantidad']},{p['precio']}\n")

def guardar_json(productos):
    with open(os.path.join(CARPETA_DATOS, "datos.json"), "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)

def guardar_csv(productos):
    with open(os.path.join(CARPETA_DATOS, "datos.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nombre", "Cantidad", "Precio"])
        for p in productos:
            writer.writerow([p['id'], p['nombre'], p['cantidad'], p['precio']])

# Guardar datos al iniciar la app
guardar_txt(productos)
guardar_json(productos)
guardar_csv(productos)

# ===== Rutas de Flask =====
@app.route('/')
def index():
    return render_template("index.html", productos=productos)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template("usuario.html", nombre=nombre)

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
