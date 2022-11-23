import pymongo
from pymongo import MongoClient
from os import system, name
def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def searchAuthors(db): 
    """
    Search for authors The user should be able to provide a keyword  and see all authors whose names contain the keyword (the matches should be case-
    insensitive). For each author, list the author name and the number of publications. The user should be able to select an author and see the title, year and
    venue of all articles by that author. The result should be sorted based on year with more recent articles shown first.
    """
    clear()
    userInput = input("Input an author's name: ").split()  # list of separated keywords
    userInput = userInput[0]  # only take the first word
    # print(userInput)
    db.dblp.drop_indexes()
    db.dblp.create_index([("authors" , pymongo.TEXT)])

    # find matches
    results = []
    results = db.dblp.find({"$text": { "$search": userInput }}).sort("year")   

    # save authors and save amount of matches
    authorDict = {}
    
    for line in results:
        author_list = line["authors"] # to make case insensitive
        for i in range(len(author_list)):
            if userInput.lower() in author_list[i].lower():
                if author_list[i] in authorDict.keys():
                    authorDict[author_list[i]] += 1
                else:
                    authorDict[author_list[i]] = 1

    
    count = 0
    author_list = []
    for match in authorDict.keys():
        print("Result #" + str(count+1))
        count += 1
        print(match)
        author_list.append(match)
        print("Number of publications:", authorDict[match], "\n")


    userInput = input("Input result number to find out more about the author")
