from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hola():
    return "<h1>Hola<h1>"
    
    
@app.route("/user/<username>")
def user(username):
    return f"<h1>Hola {escape(username)}<h1>"   
    
@app.route("/post/<int:post_id>")
def post(post_id):
    return f"<h1>post {post_id}<h1>"

@app.route("/path/<path:subpath>")
def path(subpath):
    return f"<h1>subpath {escape(subpath)}<h1>"

@app.route("/float/<float:dato>")
def float(dato):
    return f"<h1>flotante {dato}<h1>"


@app.route("/uuid/<uuid:dato>")# Es un dato especifico
def uuid(dato):
    return f"<h1>uuid {dato}<h1>"

if __name__ == '__main__':
    app.run(debug=True)