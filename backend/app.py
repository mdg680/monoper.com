import json
import flask
from flask import Flask

from db.db import Database
from db.models import Post


app = Flask(__name__)
db = Database()


# Current source: https://medium.com/@arif555/containerizing-a-full-stack-web-application-a-step-by-step-guide-e9374f748177 # noqa
@app.route("/api/posts", methods=["GET"])
def get_posts() -> flask.Response:
    """Returns a list of posts
    :returns: A list of posts
    """
    posts = db.get_posts()

    return get_json(posts)


def get_json(sql_sequence) -> json:
    """Converts a list of SQLAlchemy objects to a JSON object
    :returns: A JSON object
    """
    return [x.get_json() for x in sql_sequence]


if __name__ == "__main__":
    db.create_tables()
    five_posts = [
        Post("John Doe", "First Post", "This is the first post", "April 20, 2018"),
        Post("Jane Doe", "Second Post", "This is the second post", "April 21, 2018"),
        Post("John Doe", "Third Post", "This is the third post", "April 22, 2018"),
        Post("Jane Doe", "Fourth Post", "This is the fourth post", "April 23, 2018"),
        Post("John Doe", "Fifth Post", "This is the fifth post", "April 24, 2018"),
    ]
    db.insert(five_posts)
    app.run(debug=True, host="0.0.0.0", port=8000)
