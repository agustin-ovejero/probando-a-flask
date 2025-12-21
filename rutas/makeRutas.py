from flask import Flask
app = Flask(__name__)

# Crendo multiples rutas
@app.route("/")
def hola():
    return "<h1>Hola<h1>"

@app.route("/como-andas")
def como_andas():
    return "<h1>Como andas vos ?<h1>"


@app.route("/como-andas/chau")
def chau():
    return "<h1>Chau<h1>"