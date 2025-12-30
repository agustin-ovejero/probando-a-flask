from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>index<h1>"

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#        
#    return show_the_login_form()
    

def do_the_login():
    return "<h1>Agamos el login<h1>"

def show_the_login_form():
    return "<h1>Formulario<h1>"
    
# tambien podemos crear funciones inidivideales para diferntes tipos de verbos
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)