from flask import Flask
import os

app = Flask(__name__)
port = int(os.getenv("VCAP_APP_PORT", 5000))

@app.route('/')
def hello_world():
	return 'Hello world!\n'


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = port)



