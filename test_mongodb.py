
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://vdeogade007_db_user:@password@ac-mnblq3t-shard-00-00.dwqfnyb.mongodb.net:27017,ac-mnblq3t-shard-00-01.dwqfnyb.mongodb.net:27017,ac-mnblq3t-shard-00-02.dwqfnyb.mongodb.net:27017/?ssl=true&replicaSet=atlas-x2yupq-shard-0&authSource=admin&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)