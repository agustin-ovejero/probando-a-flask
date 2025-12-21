from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def hola():
    return "<h1>Hola<h1>" 

# cuando una ruta que puede recibir arguemento y esta de esta manera (/ruta)
# Si queremos solicitar esa ruta tenemos que pasarle si o si el argumento (/ruta?dato=xxx)
# Peor si la ruta esta de esta manera (/ruta/)
# Podemos ingresar sin pasarle argumento
# rari
@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}"

if __name__ == '__main__':
    app.run(debug=True)