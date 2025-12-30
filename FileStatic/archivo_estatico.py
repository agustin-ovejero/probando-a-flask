from flask import Flask, render_template
app =  Flask(__name__)

@app.route('/')
def index():
    # para cargar los archivos estaticos necesitamos renderizar templates
    return render_template('hola.html')
    


if __name__ == "__main__":
    app.run(debug=True)

