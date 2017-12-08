from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build_a_blog:1234@localhost:3306/build_a_blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    entry = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, entry, pub_date=None):
        self.title = title
        self.entry = entry
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date


@app.route('/')
@app.route('/blog', methods=['POST', 'GET'])
def blog():

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_entry = request.form['entry']
        print(blog_entry + " " + blog_title)

        new_blog = Blog(blog_title, blog_entry)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('blog', id=new_blog.id))

    #print(request.args)
    if request.args:
        db_id = request.args['id']
        post = Blog.query.filter_by(id=db_id).first()
        title = post.title
        entry = post.entry
        return render_template('blog.html', title=title, entry=entry)

    else:
        title = "Build-A-Blog!"
        posts = Blog.query.order_by(Blog.pub_date.desc()).all()

    return render_template('blog.html', title=title, posts=posts)



@app.route('/newpost', methods=['GET', 'POST'])
def newpost():

    return render_template('newpost.html', title="Add a Blog Entry")


if __name__ == '__main__':
    app.run(debug=True)