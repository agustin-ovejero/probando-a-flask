from flask import Flask
from flask import render_template, session

app = Flask(__name__)
app.secret_key =  '123'

@app.route('/')
def index():
    if "visits" not in session:
        session["visits"] = 1
    session["visits"] += 1
    return render_template("index.html", visits = session["visits"])


if __name__ == '__main__':
    app.run(debug=True)


