from flask import Flask, render_template
from flasked_blog.posts import Post

app = Flask(__name__)


@app.route("/")
def get_home():
    post = Post()
    return render_template("index.html", posts=post._generate_fake_posts())

@app.route("/contact")
def get_contact():
    return render_template("card.html")


if __name__ == "__main__":
    app.run(debug=True)

