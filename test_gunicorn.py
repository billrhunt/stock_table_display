
import os
from flask import Flask,render_template

#from flask_peewee.db import Database 

# database config settings
#create flask object
app = Flask(__name__)


@app.route('/')
def main():
	print('main')

@app.route('/load')
def load():
	print('load')	

