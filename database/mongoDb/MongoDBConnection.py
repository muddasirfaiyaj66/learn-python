from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("localhost",27017)
db = client.testDB
people = db.people

people.insert_one( {"Name":"Smith", "age":50})

for person in people.find():
    people.delete_one({'_id': person["_id"]})
