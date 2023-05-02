from flask import Flask, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

@app.route('/drivers', methods=['GET'])
def get_drivers():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1']
    collection = db['drivers']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)

@app.route('/circuits', methods=['GET'])
def get_circuits():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1']
    collection = db['circuits']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)

@app.route('/constructors', methods=['GET'])
def get_constructors():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1']
    collection = db['constructors']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)

@app.route('/seasons', methods=['GET'])
def get_seasons():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1']
    collection = db['seasons']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)

@app.route('/tracks', methods=['GET'])
def get_tracks():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1']
    collection = db['tracks']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
