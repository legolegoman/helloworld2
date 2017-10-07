#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
	return 'Hello Hello World 2!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)


