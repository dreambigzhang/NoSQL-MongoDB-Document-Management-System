import json
from pymongo import MongoClient

def load_json():
    json_file = input("Input a json file: ")
    port_num = input("Input a port number: ")
    client = MongoClient('mongodb://localhost:' + port_num)

    db = client['291db']

    dblp = db["dblp"]
    dblp.drop()

    data = []
    with open(json_file) as f: 
        for line in f: 
            data.append(json.loads(line.strip()))
    dblp.insert_many(data)
