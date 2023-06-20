import json
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import default


CONNECTION_STRING = "mongodb://localhost:27017"

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return default(o)

def get_client():
    '''connection to mongodb'''
    try:
        client = MongoClient(CONNECTION_STRING)
        print("Connected to MongoDB")
        return client
    except Exception as error:
        print("Could not connect to MongoDB")

def get_sql():
    '''db & collection'''
    client = get_client()
    db_collection = client['company']['employees']
    myquery = {'name.name': 'peter'}

    results = list(db_collection.find(myquery))
    result_json = json.dumps(results, cls=CustomJSONEncoder, indent=4)
    print(result_json)
    client.close()

if __name__ == "__main__":
    get_sql()