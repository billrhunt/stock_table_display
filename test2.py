

#!/bin/bash

import datetime
from pprint import pprint
import os
import sys
from flask import Flask,render_template
from flask_peewee.db import Database 

#heroku config:set DATABASE_URL='mysql://b4a011df81c9ae:18021a71@us-cdbr-iron-east-02.cleardb.net/heroku_d6b6aafc5915d9a'
DATABASE = {
	'engine': 'peewee.MySQLDatabase',
	'user': 'b4a011df81c9ae',
	'password': '18021a71',
	'host': 'us-cdbr-iron-east-02.cleardb.net',
	'name': 'heroku_d6b6aafc5915d9a',
	}

#create flask object
app = Flask(__name__)
app.config.from_object(__name__)
db = Database(app)


class Prices(db.Model):
	name = TextField()
	date = DateField ()
	price = FloatField()




@app.route('/')
def main():
	prices= read_data('msft')
	return render_template('main.html', prices=prices)

@app.route('/load')
def load():
	load_tables()
	prices= read_data('msft')
	return render_template('main.html', prices=prices)

if __name__ == '__main__':	
	app.run(debug=True)
