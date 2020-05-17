from flask import Flask

from flask import Flask, json
import requests, _json

app = Flask(__name__)

@app.route('/posts')
def get_user():

    user_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    user = user_response.json()
    response = app.response_class(
            response=json.dumps(user),
            status=200,
            mimetype='application/json')

    return response


if __name__ == "__main__":
    app.run()