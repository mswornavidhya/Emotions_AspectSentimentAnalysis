import pymongo
from pymongo import MongoClient
# import datetime
# import python-dotenv ## Python-dotenv reads key-value pairs from a . env file and can set them as environment variables.

def createCollections():
    client = MongoClient(
        "mongodb+srv://swornama:Msworna284@emotionalfreecluster.nlfh7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["testMongoDB"]
    collections = db["testConnectionPython"]

    return collections


def insert_collections(collection):
    data = [
        {"user": "Krish", "subject": "Database", "score": 80},
        {"user": "Amit", "subject": "JavaScript", "score": 90},
        {"user": "Amit", "title": "Database", "score": 85},
        {"user": "Krish", "title": "JavaScript", "score": 75},
        {"user": "Amit", "title": "Data Science", "score": 60},
        {"user": "Krish", "title": "Data Science", "score": 95}]

    collection.insert_many(data)

def delete_collections(collection):
    collection.delete_many({})
