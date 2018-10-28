from flask import Flask, render_template
from planner import algorithm, constants
from model.body import Body

app = Flask(__name__)


@app.route('/hello')
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


@app.route('/')
def test():
    value1 = Body()
    value2 = Body().show_body_status()
    return render_template(
        'test.html',
        value1=value1,
        value2=value2
    )


if __name__ == '__main__':
    app.run()
