from read_data_mysql import *


prices=read_data('msft')

for prices_row in prices:
	print('{} {}'.format(prices_row.date,prices_row.price))
