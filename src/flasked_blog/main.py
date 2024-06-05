from flask import Flask, render_template
from flask import request

from flasked_blog.posts import FakePosts
from flasked_blog import constants as c
from flasked_blog.email import send_email, get_personal_email, generate_email_content

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", posts=FakePosts().get_all_posts()[-3:])


@app.route("/contact", methods=[c.GET, c.POST])
def get_contact():
    if request.method == c.POST:
        subject, body = generate_email_content(request.form)
        send_email(subject=subject, body=body, to_emails=[get_personal_email()])
        return render_template("contact.html", method=c.POST)
    elif request.method == c.GET:
        return render_template("contact.html")
    else:
        raise ValueError("Invalid request method.")


# @app.route("/posts")
# def get_posts(post_id: int):
#     return render_template(".html", post=FakePosts().get_post_by_id(post_id))


@app.route("/posts/<int:post_id>")
def get_post(post_id: int):
    return render_template("card.html", post=FakePosts().get_post_by_id(post_id))


if __name__ == "__main__":
    app.run(debug=True)
