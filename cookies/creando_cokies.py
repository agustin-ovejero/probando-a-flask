from flask import Flask
from flask import request, make_response
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    custome_cookie = request.cookies.get('custome_cookie', 'Undefined')
    print(custome_cookie)
    return render_template('index.html')


@app.route('/cookies')
def cookies():
    response = make_response(render_template('cookies.html'))
    response.set_cookie('custome_cookie', 'Agus')
    return response

if __name__ == "__main__":
    app.run(debug=True)