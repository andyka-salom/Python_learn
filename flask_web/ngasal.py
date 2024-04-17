from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    person = {
        'name': 'John',
        'age': 25,
        'citi': 'surabaya'
    }
    return "Hello from " + person['city']