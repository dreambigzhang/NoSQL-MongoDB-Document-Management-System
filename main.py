from os import system, name
from searchArticle import searchArticle
from searchAuthors import searchAuthors
from listVenues import listVenues
from addArticle import addArticle
from load_json import load_json
from pymongo import MongoClient

def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

port_num = load_json()
client = MongoClient('mongodb://localhost:' + port_num)
db = client['291db']

def main():



    action = input("Enter\n1 Search for articles\n2 Search for authors\n3 List the venues\n4 Add an article\nAnything else to exit program \n").strip()
    if action=='1':
        endFunction= searchArticle(db)
        clear()
        if endFunction == "-1":
            client.close()
            quit()
        main()
    elif action == '2':
        endFunction = searchAuthors(db)
        clear()
        if endFunction == "-1":
            client.close()
            quit()
        main()
    elif action == '3':
        endFunction = listVenues(db)
        clear()
        if endFunction == "-1":
            client.close()
            quit()
        main()
    elif action == '4':
        endFunction = addArticle(db)
        clear()
        if endFunction == "-1":
            client.close()
            quit()
        main()
    else:
        client.close()
        quit()

if __name__ == "__main__":
    main()
