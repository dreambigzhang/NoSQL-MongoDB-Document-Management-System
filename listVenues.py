from pymongo import MongoClient
import pymongo
import json
def listVenues(db): 
    """
    List the venues The user should be able to enter a number n and see a listing of top n venues. For each venue, 
    list the venue, 
    the number of articles in that venue, and 
    the number of articles that reference a paper in that venue. Sort the result based on the number of papers that reference the venue with
    the top most cited venues shown first. 
    """
    
    print("**List Top Venues")
    
    topNum = input("Enter the number of top venues: ")
    db.dblp.create_index([("reference",pymongo.TEXT)])


    cursor = db.dblp.aggregate([
        {
            "$lookup":
                {
                    "from":"dblp",
                    "localField":"id",
                    "foreignField":"references",
                    "as":"referenced"
                }
        },
        {
            "$group" : {
                "_id" : "$venue",
                "artCount":{"$count":1},
                "refCount": {"$size":"$referenced"},#{db.dblp.count_documents({"$text": { "$search": "id"}})}
            }
        },
        {
            "$project":
                {"venue":1,"artCount":1,"refCount": 1}
        },
        { 
            "$sort": { "refCount": 1 } 
        },
        {
            "$limit": topNum
        }
    ])
    for venue in cursor:
        print(venue)
    quit()