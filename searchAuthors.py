
from os import system, name
def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def searchAuthors(db):  # returns what user wants to do after finishing from function
    """
    Search for authors The user should be able to provide a keyword  and see all authors whose names contain the keyword (the matches should be case-
    insensitive). For each author, list the author name and the number of publications. The user should be able to select an author and see the title, year and
    venue of all articles by that author. The result should be sorted based on year with more recent articles shown first.
    """
    clear()
    print("**Search Author**")
    userInput = input("Input an author's name: ").split()  # list of separated keywords
    userInput = userInput[0]  # only take the first word
    # print(userInput)

    # find matches
    results = []
    results = db.dblp.find({"$text": { "$search": userInput }}).sort("year", -1)   

    counter = 0 # check how many results we got

    # save authors and save amount of matches
    authorDict = {}
    
    for line in results:
        counter += 1
        author_list = line["authors"] # to make case insensitive
        for i in range(len(author_list)):
            if userInput.lower() in author_list[i].lower():
                if author_list[i] in authorDict.keys():
                    authorDict[author_list[i]] += 1
                else:
                    authorDict[author_list[i]] = 1

    if counter == 0: 
        finalInput = input("There were no results, enter anything to go back to main menu or enter -1 to exit program: ")
        return finalInput
    

    count = 0
    author_list = []
    for match in authorDict.keys():
        print("Result #" + str(count+1))
        count += 1
        print(match)
        author_list.append(match) # for finding author
        print("Number of publications:", authorDict[match], "\n")


    userInput = input("Input result number to find out more about the author, or anything else to continue, or -1 to exit program: ")
    try:
        if userInput == "-1":
            return userInput
        userInput = int(userInput)
    except: 
        return userInput
    chosen_author = author_list[userInput - 1]
    # results = []
    # results = db.dblp.find({"$text": { "$search": chosen_author }}).sort("year", -1) 
    # for line in results: 
    #     if chosen_author in line["authors"]:
    #         print("Title:", line["title"])
    #         print("Year:", line["year"])
    #         print("Venue:", line["venue"] , "\n")
    results = db.dblp.find({"authors":chosen_author}).sort("year", -1)
    for line in results: 
        print("Title:", line["title"])
        print("Year:", line["year"])
        print("Venue:", line["venue"] , "\n")
    
    userInput = input("Enter anything to go back to main menu or -1 to exit the program: ")
    return userInput

