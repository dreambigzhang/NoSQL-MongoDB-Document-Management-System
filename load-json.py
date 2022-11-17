import json
from pymongo import MongoClient

def load_json():
    json_file = input("Input a json file: ")
    works = 0
    while(works == 0):
        try:
            open(json_file)
            works == 1
        except: 
            works == 0
            json_file = input("Incorrect json file, try again: ")
            
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
if __name__ == "__main__":
    load_json()