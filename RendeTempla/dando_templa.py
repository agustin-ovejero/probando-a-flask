from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>index<h1>"

@app.route('/hey')
def hey():
    return "hey"


#podemos envolver una función para que reaccione para dos rutas
@app.route('/saludo/')
@app.route('/saludo/<name>')
def saludo(name=None):
    return render_template('hello.html', person=name) # lo va a buscar en la carpeta de templates

if __name__ == "__main__":
    app.run(debug=True)