from pymongo import MongoClient


client = MongoClient("mongodb+srv://nettraficuser:<password>@nettraffic.vc92v.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test
