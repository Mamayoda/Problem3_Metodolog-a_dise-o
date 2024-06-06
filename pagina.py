#pagina web front-end
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('home.html')

@app.route('/compra')
def compra():
    return 'Esta es la pagina de compra'

if __name__ == '__main__':
    app.run()