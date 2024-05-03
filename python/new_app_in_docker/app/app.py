###----------------------------------------------------
#-Owner: Alexey Krasichonak
#-Discription: Get request - show table, POST - add an object, PUT - eddit an object
###----------------------

import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')

mongo_uri = f'mongodb://{mongodb_username}:{mongodb_password}@db:27017/'

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


@app.route('/data/<id>', methods=['PUT'])
def update_data(id):
    req_data = request.get_json()
    if req_data:
        document_id = ObjectId(id)
        collection.update_one({"_id": document_id}, {"$set": req_data})
        return jsonify({"message": "Data updated successfully"}), 200
    else:
        return jsonify({"error": "No data provided"}), 400


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)


