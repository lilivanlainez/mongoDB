
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nelsonlainez91:eo71Nw0dkAnWAVxM@cluster0.bzqjn9m.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client[ "teststore"]
collection = db[ "products"]

collection.insert_one({"name":"keyboard","price": 300})

results = collection.find()

for r in results:
    print(r["name"])
