from flask import Flask, render_template, request
from redis import Redis
from matplotlib import pyplot as plt

import lib

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/graph_maker_API', methods=['POST'])
def graph_maker_API():
    if request.method != 'POST':
        return '不正なリクエストです.'
    
    errors = list()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)