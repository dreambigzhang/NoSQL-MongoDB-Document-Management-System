import pymongo
from pymongo import MongoClient
def searchArticle(port_num): 
    '''
    Search for articles The user should be able to provide one or more keywords, and the system should retrieve all articles that match all those keywords
    (AND semantics). A keyword matches if it appears in any of title, authors, abstract, venue and year fields (the matches should be case-insensitive). For
    each matching article, display the id, the title, the year and the venue fields. The user should be able to select an article to see all fields including the
    abstract and the authors in addition to the fields shown before. If the article is referenced by other articles, the id, the title, and the year of those
    references should be also listed
    '''
    client = MongoClient('mongodb://localhost:' + port_num)
    db = client['291db']

    userInput = input("Input one or more keywords all separated by a space: ")  # list of separated keywords
    # print(userInput)
    db.dblp.create_index([("abstract", pymongo.TEXT), ("authors" , pymongo.TEXT), ("title", pymongo.TEXT), ("venue", pymongo.TEXT), ("year",pymongo.TEXT)])

    results = db.dblp.find({"$text": { "$search": userInput }})   

    for line in results:
        print("Id:", line["id"])
        print("Title:", line["title"])
        print("Year:", line["year"])
        print("Venue:", line["venue"])
        print("\n")



if __name__ == "__main__":
    searchArticle("27017")