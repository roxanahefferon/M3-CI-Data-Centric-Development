import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world... again'


if __name__ == '__main__':
    host = os.environ.get('IP'),
    port = (os.environ.get('PORT')),
    debug = (True)
