from pymongo import MongoClient
import pymongo
def listVenues(db): 
    """
    List the venues The user should be able to enter a number n and see a listing of top n venues. For each venue, 
    list the venue, 
    the number of articles in that venue, and 
    the number of articles that reference a paper in that venue. Sort the result based on the number of papers that reference the venue with
    the top most cited venues shown first. 
    """
    
    print("**List Top Venues")
    
    topNum = int(input("Enter the number of top venues: "))
    db.dblp.create_index([("references",pymongo.TEXT)])
    
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
                "artCount":{"$count":{}},
                "refCount": {"$sum":{"$size":["$referenced"]}}#{db.dblp.count_documents({"$text": { "$search": "id"}})}
            }
        },

        {
            "$project":
                {"venue":1,"artCount":1, "refCount": 1} #,"refCount": 1
        },
        { 
            "$sort": { "refCount": -1 } 
        },
        {
            "$limit": topNum
        }
    ])

    for venue in cursor:
        print(venue)
    quit()

'''
{
            "$unwind":{
                "path": "$referenced"
            }
},'''
'''
{
            "$addFields":
            {
                "referenced": db.dblp.count_documents({"$text": {"$search":{"$in": "id"}}}) #db.dblp.count_documents({"$text": {"$search": "id"}})
            }
        },
'''
'''
 {
            "$addFields":
            {
                "referenced": db.dblp.count_documents({"$text": { "$search": "id"}})
            }
        },
'''
'''
        {
            "$lookup":
            {
                "from":"dblp",
                "localField":"id",
                "foreignField":"references",
                "as":"referenced"
            }
        },
       '''
'''
        {
            "$lookup": {
                "from": "dblp",
                "let": { "reference": "$reference" },
                "pipeline": [],#[{ "$match": { "$expr": { "id": {"$in": "reference" }}}}],
                "as": "referenced"
            }
        },
'''
'''
{
            "$lookup":
            {
                "from":"dblp",
                "localField":"id",
                "foreignField":"references",
                "as":"referenced"
            }
        },
'''