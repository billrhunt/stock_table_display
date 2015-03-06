import ystockquote
import urllib
from pprint import pprint
import datetime
from peewee import *
import csv

db = MySQLDatabase('stock_prices',user='billrhunt',passwd='apps4expG')

class BaseModel(Model):
	class Meta:
		database =db

class Prices(BaseModel):
	name = TextField()
	date = DateField ()
	price = FloatField()

def Init():
	"""Create the databases and tables when we start"""
	db.connect()
	db.create_tables([Prices], safe=True)

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
			if Prices.select().where( Prices.name == stock).where(Prices.date==date_object).count() == 0 :
				Prices.create(name = stock ,price = results[stock][date]['Close'], date = date_object)
	
			

def read_data(stock_name):
	"""read from database"""
	return Prices.select().where(Prices.name == stock_name)

Init()

load_tables()


