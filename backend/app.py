import flask
from flask import Flask, jsonify  # , render_template, request

app = Flask(__name__)
# Current source: https://medium.com/@arif555/containerizing-a-full-stack-web-application-a-step-by-step-guide-e9374f748177
@app.route('/api/posts', methods=['GET'])
def get_posts() -> flask.Response:
    """ Returns a list of posts
        :returns: A list of posts
    """
    return jsonify(
        [
            {
                'author': 'John Doe',
                'title': 'First Post',
                'content': 'This is the first post',
                'date_posted': 'April 20, 2018'
            },
            {
                'author': 'Jane Doe',
                'title': 'Second Post',
                'content': 'This is the second post',
                'date_posted': 'April 21, 2018'
            }
        ]
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)