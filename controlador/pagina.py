#pagina web front-end
from flask import Flask, render_template, request, redirect, Response, session
from flask_mysqldb import MySQL, MySQLdb
app = Flask(__name__, template_folder='../vista/template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tienda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST' and 'txtNombre' in request.form and 'txtID':
        _Nombre = request.form['txtNombre']
        _ID = request.form['txtID']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM comprador WHERE nombreComprador= %s AND idComprador= %s",(_Nombre,_ID))
        account = cur.fetchone()

        if account:
            session['logueado'] = True
            session['ID'] = account['idComprador']
            session['Nombre'] = account['nombreComprador']
            return redirect('/home')
        else:
            return render_template('login.html', msg='Nombre o ID incorrecto')
    return render_template('login.html')
    

@app.route('/home')
def home():
    if 'logueado' in session:
        return render_template('home.html', nombre=session['Nombre'])
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)