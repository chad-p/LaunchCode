from flask import Flask, request, redirect, render_template, url_for, make_response, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:1234@localhost:3306/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(50))
    signup_date = db.Column(db.DateTime)

    def __init__(self, username, password, signup_date=None):
        self.username = username
        self.password = password
        if signup_date is None:
            signup_date = datetime.utcnow()
        self.signup_date = signup_date


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    entry = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    username = db.Column(db.Integer)

    def __init__(self, title, entry, username, pub_date=None):
        self.title = title
        self.entry = entry
        self.username = username
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date


@app.route('/')
@app.route('/index')
def index():

    if 'username' in session:
        print("[index] logged in as " + session['username'])

    users = User.query.order_by(User.signup_date.desc()).all()
    print(users)

    return render_template('index.html', users=users)


@app.route('/blog', methods=['POST', 'GET'])
def blog():

    if 'username' in session:
        print("[blog] logged in as " + session['username'])

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_entry = request.form['entry']
        username = session['username']
        blog_user = User.query.filter_by(username=username).first()
        print(blog_user)
        print(blog_entry + " " + blog_title)

        new_blog = Blog(blog_title, blog_entry, blog_user.id)
        print(new_blog)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('blog', id=new_blog.id))

    print(request.args)
    if request.args:

        print(request.args)

        if 'id' in request.args:
            db_id = request.args['id']
            post = Blog.query.filter_by(id=db_id).first()
            username = User.query.filter_by(id=post.username).first()
            return render_template('blog.html', post=post, username=username.username)

        elif 'user' in request.args:
            db_user = request.args['user']
            print(db_user)
            #posts = Blog.query.filter_by(username="1").all()
            posts = db.session.query(Blog.id, Blog.title, Blog.entry, Blog.username, User.username).filter(Blog.username == User.id).filter(User.username==db_user)
            print(posts)
            print(posts.statement)

            return render_template('blog.html', posts=posts)

    else:
        posts = db.session.query(Blog.id, Blog.title, Blog.entry, Blog.username, User.username)\
            .filter(Blog.username == User.id).order_by(Blog.pub_date.desc()).all()

    return render_template('blog.html', posts=posts)



@app.route('/blog/newpost', methods=['GET', 'POST'])
def newpost():
    if 'username' in session:
        print("[newpost] logged in as " + session['username'])
        return render_template('newpost.html')

    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=session['username']).first()
        user_password = user.password

        if user_password != password:
            wrong_pwd = "Incorrect password entered."
            return render_template('login.html', wrong_pwd=wrong_pwd)

        print("[login] logged in as " + session['username'])
        return redirect(url_for('newpost'))

    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('blog'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        print(username + " " + password)

        if not password == verify:
            verify_error = "Passwords Don't Match"
            return render_template('signup.html', verify_error=verify_error)

        existing_user = User.query.filter_by(username=username).first()

        if not existing_user:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = request.form['username']
            return redirect(url_for('newpost', user=new_user.username))
        else:
            username_error = "A user with that username already exists"
            return render_template('signup.html', username_error=username_error)

    return render_template('signup.html')

# set the secret key.  keep this really secret:
app.secret_key = '1234'


if __name__ == '__main__':
    app.run(debug=True)