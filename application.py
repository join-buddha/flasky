from flask import Flask, render_template
from flask_bootstrap import Bootstrap

application = app = Flask(__name__)
boostrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name.capitalize())
"""
some changes made
"""
