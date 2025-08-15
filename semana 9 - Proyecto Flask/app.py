from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola! Bienvenido a mi aplicación Flask.'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Bienvenido, {nombre}!'

@app.route('/usuario')
def usuario_fijo():
    return 'Bienvenido, Karen Aguinda!'

if __name__ == '__main__':
    app.run(debug=True)
