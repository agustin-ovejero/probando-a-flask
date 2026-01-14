from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello world<h1>"

@app.route('/me')
def me_api():
    user = get_current_user()
    return {
        "username": user[0],
        "theme": user[1],
        "image": user[2]
    }
    

@app.route('/usuario')
def usuario():
    usu = get_current_user()
    return jsonify(usu)



def get_current_user():
    return ["agus", "los redondos", "imagen"]

if __name__ == '__main__':
    app.run(debug=True)

