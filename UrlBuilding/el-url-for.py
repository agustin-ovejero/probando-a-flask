from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index')) # Lo primera keyworld que recibe ulr_for es el nombre de la función
    print(url_for('login')) # se utiliza mas en jinja
    print(url_for('login', next='/'))
    print(url_for('profile', username='john doe'))
if __name__ ==  '__main__':
    app.run(debug=True)
    