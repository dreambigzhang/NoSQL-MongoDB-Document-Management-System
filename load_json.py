import json
from pymongo import MongoClient

def load_json():
    json_file = input("Input a json file: ")
    while(1):
        try: 
            open(json_file)
            break
        except:
            json_file = input("Invalid file, input a valid file: ")
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
    #for line in data:  to visualize what is happening
       #print(line)
       #print()

    return port_num  # to get port number and connect
if __name__ == "__main__":
    load_json()