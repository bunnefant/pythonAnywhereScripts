import json
from flask import Flask


app = Flask(__name__)
list = {'data' : []}

@app.route('/hello')
def hello_world():
    return 'Hello from Flask!'

@app.route('/benzingaCall')
def benzingaCall():
    return list

if __name__ == "__main__":
    app.run()
