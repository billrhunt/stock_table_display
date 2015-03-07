
import os
from flask import Flask,render_template
from read_data_mysql import *
from load_data_mysql import * 
import urlparse
from flask_peewee.db import Database 

# database config settings
	}
#create flask object
app = Flask(__name__)


@app.route('/')
def main():
	prices= read_data('msft')
	return render_template('main.html', prices=prices)

@app.route('/load')
def load():
	load_tables()
	

