from flask import Flask, render_template, redirect, request, session, url_for
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('signup'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        return redirect(url_for('welcome', username=username))

    return render_template('signup.html')


@app.route('/welcome')
def welcome():
    return request.args['username']


if __name__ == '__main__':
    app.run(debug=True)
