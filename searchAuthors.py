import pymongo
from pymongo import MongoClient
from os import system, name
def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def searchAuthors(port_num): 
    """
    Search for authors The user should be able to provide a keyword  and see all authors whose names contain the keyword (the matches should be case-
    insensitive). For each author, list the author name and the number of publications. The user should be able to select an author and see the title, year and
    venue of all articles by that author. The result should be sorted based on year with more recent articles shown first.
    """
    clear()
    client = MongoClient('mongodb://localhost:' + port_num)
    db = client['291db']

    userInput = input("Input one or more keywords all separated by a space: ")  # list of separated keywords
    # print(userInput)
    db.dblp.create_index([("authors" , pymongo.TEXT)])

    results = []
    results = db.dblp.find({"$text": { "$search": userInput }})   