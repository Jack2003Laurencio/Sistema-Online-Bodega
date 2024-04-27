from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, IntegerField
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = '3.146.178.7'
app.config['MYSQL_USER'] = 'paolo'
app.config['MYSQL_PASSWORD'] = 'Paolo_Marcelo#11'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'stocks'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

#Products
@app.route('/products')
def products():
    cur=mysql.connection.cursor()
    result = cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    if result>0:
        return render_template('products.html', products = products)
    else:
        msg='Productos no hallados'
        return render_template('products.html', msg=msg)
    cur.close()

@app.route('/locations')
def locations():
    cur=mysql.connection.cursor()
    result = cur.execute("SELECT * FROM locations")

    locations = cur.fetchall()

    if result>0:
        return render_template('locations.html', locations = locations)
    else:
        msg='Ubicación no encontrada'
        return render_template('locations.html', msg=msg)
    cur.close()

@app.route('/product_movements')
def product_movements():
    #create cursor
    cur=mysql.connection.cursor()

    #Get products
    result = cur.execute("SELECT * FROM productmovements")

    movements = cur.fetchall()

    if result>0:
        return render_template('product_movements.html', movements = movements)
    else:
        msg='Movimiento de producto no encontrada'
        return render_template('product_movements.html', msg=msg)
    #close connection
    cur.close()

