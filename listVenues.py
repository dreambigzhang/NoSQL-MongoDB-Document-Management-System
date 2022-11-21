from pymongo import MongoClient
import json
def listVenues(db): 
    """
    List the venues The user should be able to enter a number n and see a listing of top n venues. For each venue, 
    list the venue, 
    the number of articles in that venue, and 
    the number of articles that reference a paper in that venue. Sort the result based on the number of papers that reference the venue with
    the top most cited venues shown first. 
    """
    f = open('dblp-ref-1k.json')
    articlesJson = json.load(f)
    
    articles = db["articles"]
    articles.insert_many(articlesJson)

    print("**List Top Venues")
    topNum = input("Enter the number of top venues: ")

    cursor = articles.aggregate([
        {
            "$group" : { 
                "_id" : "$venue",
                "artCount":{"$count":1},
                "refCount": {articles.find({"$reference":"id"}).count()}
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
    quit()