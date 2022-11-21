import pymongo
from pymongo import MongoClient
from os import system, name
def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



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
    db.dblp.create_index([("abstract", pymongo.TEXT), ("authors" , pymongo.TEXT), ("title", pymongo.TEXT), ("venue", pymongo.TEXT), ("year",pymongo.TEXT)])

    results = []
    results = db.dblp.find({"$text": { "$search": userInput }})   

    indexCounter = 0
    resultList = []
    for line in results:
        resultList.append(line)
        print("Result #" + str(indexCounter + 1))
        indexCounter += 1
        print("Id:", line["id"])
        print("Title:", line["title"])
        print("Year:", line["year"])
        print("Venue:", line["venue"])
        print()

    selection = input("Input result number to see more about it. Or input anything else to exit: ")
    while(1): 
        try:
            selection = int(selection) 
        except: 
            break
        try:  #doesnt fully work
            selectAns = resultList[selection -1]
            print("Id:", selectAns["id"])
            print("Title:", selectAns["title"])
            print("Year:", selectAns["year"])
            print("Venue:", selectAns["venue"])
            print("Abstract:", selectAns["abstract"])
            print("Authors:", ", ".join(selectAns["authors"]))
            print()
            break
        except Exception as e: 

            print(e)
            selection = input("Result number doesn't exist, input again: ")


if __name__ == "__main__":
    searchArticle("27017")