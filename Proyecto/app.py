import os
import json
import csv
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_user_by_email, get_user_by_id, Usuario
from conexion.conexion import get_connection

app = Flask(__name__)
app.secret_key = "clave_secreta"

# =================== CONFIGURACIÓN LOGIN ===================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

# =================== PRODUCTOS ===================
CARPETA_DATOS = "datos"
if not os.path.exists(CARPETA_DATOS):
    os.makedirs(CARPETA_DATOS)

productos = [
    {"id": "G001", "nombre": "Google Pixel 4", "cantidad": 10, "precio": 60.0, "imagen": "Google Pixel 4.jpg"},
    {"id": "G002", "nombre": "Google Pixel 6 Pro", "cantidad": 5, "precio": 95.0, "imagen": "Google Pixel 6 Pro.jpg"},
    {"id": "G003", "nombre": "Google Pixel 6", "cantidad": 7, "precio": 100.0, "imagen": "Google Pixel 6.jpg"},
    {"id": "G004", "nombre": "Google Pixel 7 Pro", "cantidad": 4, "precio": 95.0, "imagen": "Google Pixel 7 Pro.jpg"},
    {"id": "H001", "nombre": "Honor 10 Lite", "cantidad": 8, "precio": 40.0, "imagen": "Honor 10 Lite.jpg"},
    {"id": "H002", "nombre": "Honor 200 Lite", "cantidad": 6, "precio": 65.0, "imagen": "Honor 200 Lite.jpg"}
]

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

guardar_txt(productos)
guardar_json(productos)
guardar_csv(productos)

# =================== RUTAS PÚBLICAS ===================
@app.route("/")
def index():
    return render_template("index.html", productos=productos)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return render_template("usuario.html", nombre=nombre)

# =================== RUTAS LOGIN ===================
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                       (nombre, email, password))
        conn.commit()
        cursor.close()
        conn.close()
        
        flash("Usuario registrado con éxito. Inicia sesión.")
        return redirect(url_for("login"))
    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("protegido"))
        else:
            flash("Credenciales incorrectas")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/protegido")
@login_required
def protegido():
    return f"Bienvenido {current_user.nombre}, esta es una ruta protegida."

# =================== MAIN ===================
if __name__ == "__main__":
    app.run(debug=True)