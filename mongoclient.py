from pymongo import MongoClient


client = MongoClient("mongodb+srv://covid19:covid19@cluster0.rhs0t.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test
