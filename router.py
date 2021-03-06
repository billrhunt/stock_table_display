

from peewee import *
import datetime
from pprint import pprint
import os
import sys
from flask import Flask,render_template
from flask_peewee.db import Database 
import ystockquote 

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


Prices.create_table(fail_silently=True)


def load_tables():
	stock_list = ['Googl','msft','spy']
	start_date ='2013-01-01'
	end_date =  datetime.datetime.now().strftime('%Y-%m-%d')

	results={}

	for stock in stock_list:
		results[stock]=ystockquote.get_historical_prices(stock,start_date,end_date)
	
		pprint(results[stock])
		for date in results[stock]:
			date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
			if Prices.select().where(Prices.name==stock).where(Prices.date==date_object).count() == 0 :
				Prices.create(name = stock ,price = results[stock][date]['Close'], date = date_object)
	return


def read_data(stock_name):
	"""read from database"""
	return Prices.select().where(Prices.name == stock_name).order_by(Prices.date.desc())


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
