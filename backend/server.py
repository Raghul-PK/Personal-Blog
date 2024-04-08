from flask import Flask, request, jsonify
import json, os

from datetime import datetime

app = Flask(__name__)

from flask import Flask, jsonify

app = Flask(__name__)

# Sample posts data
posts = [
    {"id": 1, "title": "Post 1", "content": "Content of post 1", "date": "2024-04-08"},
    {"id": 2, "title": "Post 2", "content": "Content of post 2", "date": "2024-04-09"},
    # Add more posts here as needed
]

# Route to serve posts data
@app.route('/posts')
def get_posts():
    return jsonify(posts)

@app.route('/addpost', methods=['POST'])
def create_post():
    data = request.json
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    data['time'] = formatted_datetime
    print(data)
    # Write JSON data to a file
    with open("posts/data.json", "w") as file:
        json.dump(data, file)
    return jsonify({'message': 'Post created successfully'}), 201

if __name__=='__main__':
    app.run(debug=True)