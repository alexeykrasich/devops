import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')

mongo_uri = f'mongodb://{mongodb_username}:{mongodb_password}@localhost:27017/'

client = MongoClient(mongo_uri)
db = client['database'] 
collection = db['collection']


@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)


@app.route('/data', methods=['POST'])
def add_data():
    req_data = request.get_json()
    if req_data:
        collection.insert_one(req_data)
        return jsonify({"message": "Data added successfully"}), 201
    else:
        return jsonify({"error": "No data provided"}), 400


@app.route('/data/<key>', methods=['PUT'])
def update_data(key):
    req_data = request.get_json()
    if req_data:
        collection.update_one({"key": key}, {"$set": req_data})
        return jsonify({"message": "Data updated successfully"}), 200
    else:
        return jsonify({"error": "No data provided"}), 400


if __name__ == '__main__':
    app.run(port=8080)