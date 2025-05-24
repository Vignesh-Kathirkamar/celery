# app.py
from flask import Flask, request, jsonify
from celery_config import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = make_celery(app)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    x = data['x']
    y = data['y']
    task = add_numbers.delay(x, y)
    return jsonify({'task_id': task.id}), 202

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

@celery.task
def add_numbers(x, y):
    return x + y

if __name__ == '__main__':
    app.run(debug=True)