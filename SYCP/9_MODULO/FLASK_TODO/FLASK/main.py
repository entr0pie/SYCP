from sre_parse import FLAGS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request



APP = Flask(__name__)
DB = SQLAlchemy(APP)

APP.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite3"

class Post(DB.Model):
    id = DB.Column(DB.Integer(), primary_key=True)
    title = DB.Column(DB.String())
    content = DB.Column(DB.String())
    author = DB.Column(DB.String())

@APP.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@APP.route("/post/add", methods=["POST"])
def add_post():
    try:
        form = request.form
        post = Post(title=form["title"], content=form["content"], author=form["author"])
        DB.session.add(post)
        DB.session.commit()
    except Exception as error:
        print("Error", error)

    return redirect(url_for("home"))

@APP.route("/post/<id>/del")
def delete_post(id):
    try:
        post = Post.query.get(id)
        DB.session.delete(post)
        DB.session.commit()
    except Exception as error:
        print("Error", error)

    return redirect(url_for("home"))


@APP.route("/post/<id>/edit", methods=["POST", "GET"])
def edit_post(id):
    if request.method == "POST":
        try:
            post = Post.query.get(id)
            form = request.form
            post.title = form["title"]
            post.content = form["content"]
            post.author = form["author"]
            DB.session.commit()
        except Exception as error:
            print("Error", error)

        return redirect(url_for("home"))
    else:
        try:
            post = Post.query.get(id)
            return render_template("edit.html", post=post)
        except Exception as error:
            print("Error", error)

    return redirect(url_for("home"))

DB.create_all()
APP.run(debug=True)