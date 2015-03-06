
from flask import Flask,render_template
from read_data_mysql import *

app = Flask(__name__)

@app.route('/')
def main():
	prices= read_data('msft')
	return render_template('main.html', prices=prices)

if __name__ == '__main__':
	app.run(debug=True)
