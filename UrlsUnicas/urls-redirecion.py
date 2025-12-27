from flask import Flask 
app =  Flask(__name__)

@app.route('/')
def hola():
    return "<h1>hola</h1>"

@app.route('/about')
def about():
    return "<h1>Esto es sobre...</h1>"

@app.route("/project/")
def projectos():
    return "<h1>los projectos son...</h1>"

@app.route("/project/in-progres/")
def in_progres():
    return "<h1>los projectos en progreso son...</h1>"

if __name__ == '__main__':
    app.run(debug=True)