from flask import Flask 
from flask import abort, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    abort(401)
    no_es_ejecutado()



@app.errorhandler(401) # esta es una forma de decorar los errores 
def page_not_found(error):
    return render_template('error_pagin.html'), 404
    
if __name__ == "__main__":
    app.run(debug=True)