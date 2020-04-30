from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User-agent')
    return '<p>Your browser agent is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<H1>Hello, {}!</H1>'.format(name)


