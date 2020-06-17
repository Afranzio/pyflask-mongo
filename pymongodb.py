from pymongo import MongoClient

client = MongoClient("mongodb://afranzio:6264@cluster0-shard-00-00-3ld0v.gcp.mongodb.net:27017,cluster0-shard-00-01-3ld0v.gcp.mongodb.net:27017,cluster0-shard-00-02-3ld0v.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client.get_database("MongoDB")

records = db.Learning

def DB_data(name,email,password):
    data={
        "name":name,
        "email":email,
        "pwd" : password
    }
    records.insert_one(data)