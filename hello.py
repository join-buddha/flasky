from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)
@app.route('/')
def index():
    response = make_response('<h2>This document carries a coockie</h2>')
    response.set_cookie('answer','42')
    return response
"""
    user_agent = request.headers.get('User-agent')
    return '<p>Your browser agent is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<H1>Hello, {}!</H1>'.format(name)
"""

