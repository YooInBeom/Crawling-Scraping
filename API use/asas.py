from pymongo import MongoClient

client = MongoClient()

db = client.test_database

print(db.command("collstats", "test_collection"))