from flask import Flask, request, jsonify
import json, os

from datetime import datetime, timedelta

app = Flask(__name__)

# Route to serve posts data
@app.route('/posts')
def get_posts():
    print(os.listdir("./posts"))
    all_posts = []
    for f in os.listdir("./posts"):
        file_name = "./posts/" + f
        with open(file_name, "r") as file:
            data = json.load(file)
        all_posts.append(data)
    print(all_posts)
    return jsonify(all_posts)

@app.route('/addpost', methods=['POST'])
def create_post():
    data = request.json
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    data['date'] = formatted_datetime
    print(data)
    # Write JSON data to a file
    file_name = "posts/" + data['date'] + ".json"
    with open(file_name, "w") as file:
        json.dump(data, file)
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/validate_password', methods=['POST'])
def login():
    password = request.json.get('password')
    print(password)
    if password == '1234':
        return jsonify({'authenticated': True}), 200
    else:
        return jsonify({'authenticated': False}), 401

if __name__=='__main__':
    app.run(debug=True)