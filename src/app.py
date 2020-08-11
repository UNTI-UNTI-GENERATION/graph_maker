from flask import Flask, render_template, request
from redis import Redis
from matplotlib import pyplot as plt

from lib import utility

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET' and request.args.get('mode') == 'download':
        csv = utility.get_csv_template()
        return csv
    else:
        graph_histories = [
            {
                'src':'test src',
                'name':'test name',
                'date':'YYYY-MM-DD H:i:s'
            }
        ]
        graph_src = 'https://i.gzn.jp/img/2019/06/17/poop-transplants-transmit-deadly-superbugs/00_m.jpg'
        return render_template('index.html', graph_src=graph_src, graph_histories=graph_histories)

@app.route('/graph_maker_API', methods=['POST'])
def graph_maker_API():
    if request.method != 'POST':
        return '不正なリクエストです.'
    
    errors = list()

@app.route('/latex_maker', methods=['POST'])
def latex_maker():
    if request.method != 'POST':
        return '不正なリクエストです.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)