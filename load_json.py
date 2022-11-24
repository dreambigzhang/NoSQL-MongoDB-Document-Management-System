import json
from pymongo import MongoClient
import pymongo
import os
def load_json():
    
    port_num = input("Input a port number: ")
    client = MongoClient('mongodb://localhost:' + port_num)

    db = client['291db']

    dblp = db["dblp"]
    dblp.drop()

    json_file = input("Input a json file: ")
    os.system('mongoimport --db=db --collection=dblp --type=json '+json_file.strip())
    '''
    while(1):
        try: 
            open(json_file)
            break
        except:
            json_file = input("Invalid file, input a valid file: ")

    

    data = []
    with open(json_file) as f: 
        for line in f: 
            data.append(json.loads(line.strip()))

    dblp.insert_many(data)
    dblp.update_many({},[{ "$set": {"year": { "$toString": "$year" } } }]
)
    '''
    dblp.create_index([("abstract", pymongo.TEXT), ("authors" , pymongo.TEXT), ("title", pymongo.TEXT), ("venue", pymongo.TEXT), ("year",pymongo.TEXT), ("references", pymongo.TEXT)],default_language = "none")
    #for line in data:  to visualize what is happening
       #print(line)
       #print()

    return port_num  # to get port number and connect
if __name__ == "__main__":
    load_json()