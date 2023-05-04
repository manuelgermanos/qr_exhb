from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/drivers', methods=['GET'])
def get_drivers():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1_2']
    collection = db['drivers']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)


@app.route('/constructors', methods=['GET'])
def get_constructors():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1_2']
    collection = db['constructors']
    data = []
    for doc in collection.find():
        del doc['_id'] # remove the ObjectId field from each document
        data.append(doc)
    return jsonify(data)


@app.route('/redbull', methods=['GET'])
def get_redbull():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1_2']
    constructors_collection = db['constructors']
    drivers_collection = db['drivers']
    drives_for_collection = db['drivesFor']

    # Find the Red Bull constructor by constID
    redbull_constructor = constructors_collection.find_one({"constID": "redbull"})
    constructor_data = {
        "fullname": redbull_constructor["fullname"],
        "nationality": redbull_constructor["nationality"],
        "wins": redbull_constructor["wins"],
        "pole": redbull_constructor["pole"],
        "podiums": redbull_constructor["podiums"],
        "championships": redbull_constructor["championships"],
        "goldenDriver": redbull_constructor["goldenDriver"]
    }

    # Find the drivers for the Red Bull constructor using the drivesFor collection
    redbull_driver_ids = [d["driverID"] for d in drives_for_collection.find({"constID": "redbull"})]
    driver_data = []
    for driver_id in redbull_driver_ids:
        driver = drivers_collection.find_one({"driverID": driver_id})
        driver_data.append({
            "name": f"{driver['fname']} {driver['lname']}",
            "number": driver['number'],
            "nationality": driver['nationality'],
            "bio": driver['bio'],
            "racewins": driver['racewins'],
            "podiums": driver['podiums'],
            "pole": driver['pole'],
            "points": driver['points'],
            "picture": driver['picture']
        })

    return jsonify({
        "constructor": constructor_data,
        "drivers": driver_data
    })

@app.route('/ferrari', methods=['GET'])
def get_ferrari():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1_2']
    constructors_collection = db['constructors']
    drivers_collection = db['drivers']
    drivesFor_collection = db['drivesFor']

    # Find the Ferrari constructor by constructorRef
    ferrari_constructor = constructors_collection.find_one({"constID": "ferrari"})
    constructor_data = {
        "fullname": ferrari_constructor["fullname"],
        "nationality": ferrari_constructor["nationality"],
        "wins": ferrari_constructor["wins"],
        "pole": ferrari_constructor["pole"],
        "podiums": ferrari_constructor["podiums"],
        "championships": ferrari_constructor["championships"],
        "goldenDriver": ferrari_constructor["goldenDriver"]
    }

    # Find the drivers for the Ferrari constructor by constID and driverID
    ferrari_drivers = drivers_collection.find({"driverID": {"$in": [df["driverID"] for df in drivesFor_collection.find({"constID": "ferrari"})]}})
    driver_data = []
    for driver in ferrari_drivers:
        driver_data.append({
            "name": f"{driver['fname']} {driver['lname']}",
            "number": driver['number'],
            "nationality": driver['nationality'],
            "bio": driver['bio'],
            "racewins": driver['racewins'],
            "podiums": driver['podiums'],
            "pole": driver['pole'],
            "points": driver['points']
        })

    return jsonify({
        "constructor": constructor_data,
        "drivers": driver_data
    })

@app.route('/mercedes', methods=['GET'])
def get_mercedes():
    client = MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1?retryWrites=true&w=majority")
    db = client['f1_2']
    constructors_collection = db['constructors']
    drivers_collection = db['drivers']
    drivesFor_collection = db['drivesFor']

    # Find the Mercedes constructor by constructorRef
    mercedes_constructor = constructors_collection.find_one({"constID": "mercedes"})
    constructor_data = {
        "fullname": mercedes_constructor["fullname"],
        "nationality": mercedes_constructor["nationality"],
        "wins": mercedes_constructor["wins"],
        "pole": mercedes_constructor["pole"],
        "podiums": mercedes_constructor["podiums"],
        "championships": mercedes_constructor["championships"],
        "goldenDriver": mercedes_constructor["goldenDriver"]
    }

    # Find the drivers for the Mercedes constructor by constID and driverID
    mercedes_drivers = drivers_collection.find({"driverID": {"$in": [df["driverID"] for df in drivesFor_collection.find({"constID": "mercedes"})]}})
    driver_data = []
    for driver in mercedes_drivers:
        driver_data.append({
            "name": f"{driver['fname']} {driver['lname']}",
            "number": driver['number'],
            "nationality": driver['nationality'],
            "bio": driver['bio'],
            "racewins": driver['racewins'],
            "podiums": driver['podiums'],
            "pole": driver['pole'],
            "points": driver['points']
        })
   
    return jsonify({
        "constructor": constructor_data,
        "drivers": driver_data
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
