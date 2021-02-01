#!/usr.bin/python
#-*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD'] = 'Mess1fan'
app.config['MYSQL_DB']='crypto'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)