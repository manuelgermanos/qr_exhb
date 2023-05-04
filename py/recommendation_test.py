import pymongo

# Prompt the user to enter the constID
constID = input("Enter the constID: ")

# Create a MongoClient and connect to the database
client = pymongo.MongoClient("mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/f1_2?retryWrites=true&w=majority")
db = client.f1_2

# Query the constructors collection and retrieve the data for the specified constID
result = db.constructors.find_one({"constID": constID}, {"_id": 0})

# Print the result
print(result)
