from flask import Flask
#import baseCode
import matchingEnteries
app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/assingment')
def hello():
