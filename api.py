import json
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/posts/')
def get_blog_posts():

    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    posts = posts_response.json()
    response = app.response_class(

            response=json.dumps(posts),
            status=200,
            mimetype='application/json')

    return response

@app.route('/posts/<user_id>')
def get_id(user_id):

    id_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + user_id)
    id = id_response.json()
    response = app.response_class(

            response=json.dumps(id),
            status=200,
            mimetype='application/json')

    return response

@app.route('/posts-by-userId/<user_Id>')
def get_user_id(user_Id):

    id_response = requests.get('https://jsonplaceholder.typicode.com/posts/?userId='+user_Id)
    id = id_response.json()
    response = app.response_class(

            response=json.dumps(id),
            status=200,
            mimetype='application/json')

    return response

@app.route('/posts/<user_Id>/comments')
def get_user_comments(user_Id):

    comments_response = requests.get('https://jsonplaceholder.typicode.com/posts/'+user_Id+"/comments")
    comments = comments_response.json()
    response = app.response_class(

            response=json.dumps(comments),
            status=200,
            mimetype='application/json')

    return response

if __name__ == "__main__":
    app.run()