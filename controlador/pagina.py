#pagina web front-end
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'tienda'
mysql = MySQL(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        nombreComprador = request.form['nombreComprador']
        idComprador = request.form['idComprador']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE usuario = %s AND password = %s', (nombreComprador, idComprador))
        nombreComprador = cur.fetchall()
        if nombreComprador:
            return 'usuario logeado'
        else:
            return 'usuario no logeado'
    return render_template('login.html')

@app.route('/home')
def inicio():
    return render_template('home.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
