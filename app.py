from flask import Flask 

#create app
app = Flask(__name__)

#create root (Starting point)
@app.route('/')

def hello_world():
    return 'Hello world'


