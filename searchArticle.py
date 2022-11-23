import pymongo
from pymongo import MongoClient
from os import system, name
def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

PYTHONDONTWRITEBYTECODE=1

def searchArticle(db): 
    '''
    Search for articles The user should be able to provide one or more keywords, and the system should retrieve all articles that match all those keywords
    (AND semantics). A keyword matches if it appears in any of title, authors, abstract, venue and year fields (the matches should be case-insensitive). For
    each matching article, display the id, the title, the year and the venue fields. The user should be able to select an article to see all fields including the
    abstract and the authors in addition to the fields shown before. If the article is referenced by other articles, the id, the title, and the year of those
    references should be also listed
    '''


    userInput = input("Input one or more keywords all separated by a space: ")  # list of separated keywords
    clear()
    # print(userInput)
    db.dblp.drop_indexes()
    db.dblp.create_index([("abstract", pymongo.TEXT), ("authors" , pymongo.TEXT), ("title", pymongo.TEXT), ("venue", pymongo.TEXT), ("year",pymongo.TEXT)])

    results = []
    results = db.dblp.find({"$text": { "$search": userInput }})   

    indexCounter = 0
    resultList = []
    for line in results:
        resultList.append(line)  # to pick out result later
        print("Result #" + str(indexCounter + 1))
        indexCounter += 1
        print("Id:", line["id"])
        print("Title:", line["title"])
        print("Year:", line["year"])
        print("Venue:", line["venue"] , "\n")

    selection = input("Input result number to see more about it. Or input anything else to exit: ")
    clear()
    selection_ID = 0 
    while(1):  
        # see if int
        try:
            selection = int(selection) 
        except: 
            return

        # upload results
        try:
            selectAns = resultList[selection -1]
            selection_ID = selectAns["id"]
            print("Id:", selectAns["id"])
            print("Title:", selectAns["title"])
            print("Year:", selectAns["year"])
            print("Venue:", selectAns["venue"])
            print("Abstract:", selectAns["abstract"])
            print("Authors:", ", ".join(selectAns["authors"]) , "\n")
            break
        except Exception as e: 
            # number out of bounds
            selection = input("Result number doesn't exist, input again, or input anything else to exit: ")

    db.dblp.drop_indexes()  
    db.dblp.create_index([("references", pymongo.TEXT)])   
    references = db.dblp.find({"$text": { "$search": selection_ID }})

    # print("This article is referenced by these articles:")
    for line in references: 
        if(selection_ID in line["references"]):
            print("Id:", line["id"])
            print("Title:", line["title"])
            print("Year:", line["year"], "\n")

if __name__ == "__main__":
    searchArticle("27017")