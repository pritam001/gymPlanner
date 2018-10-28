from flask import Flask, render_template
from planner import algorithm, constants

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/planner/')
@app.route('/planner/<username>')
def hello(username="Guest"):
    one_hot_encoded_weekdays = constants.one_hot_encoded_weekdays()
    return render_template(
        'planner.html',
        username=username,
        one_hot_encoded_weekdays=one_hot_encoded_weekdays
    )


if __name__ == '__main__':
    app.run()
