
import os
from flask import Flask,render_template
from read_data_mysql import *
from load_data_mysql import * 
import urlparse
from flask_peewee.db import Database 

# database config settings
urlparse.users_netloc.append('mysql')
url = urlparse.urlparse(os.environ['DATABASE_URL'])

DATABASE = {
	'engine': 'peewee.MySQLDatabase',
	'NAME': url.path[1:],
	'USER': url.username,
	'password': url.password,
	'host': url.hostname,
	'port': url.port
	}
#create flask object
app = Flask(__name__)
app.config.from_object(__name__)
db=Database(app)


@app.route('/')
def main():
	prices= read_data('msft')
	return render_template('main.html', prices=prices)

@app.route('/load')
def load():
	load_tables()
	

