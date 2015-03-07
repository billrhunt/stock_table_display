import ystockquote
import urllib
from pprint import pprint
import datetime
from peewee import *
import csv

#db = MySQLDatabase('stock_prices',user='billrhunt',passwd='apps4expG')

#jclass BaseModel(Model):
#	class Meta:
#		database = db

def Init():
	"""Create the databases and tables when we start"""
	db.connect()


def read_data(stock_name):
	"""read from database"""
	return Prices.select().where(Prices.name == stock_name).order_by(Prices.date.desc())



