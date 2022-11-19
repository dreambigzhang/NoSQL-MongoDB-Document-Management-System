from os import system, name
from searchArticle import searchArticle
from searchAuthors import searchAuthors
from listVenues import listVenues
from addArticle import addArticle
def clear(): # need to test this works on lab machine
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    action = input("Enter\n1 Search for articles\n2 Search for authors\n3 List the venues\n4 Add an article\nAnything else to exit program \n").strip()
    if action=='1':
        searchArticle()
        clear()
        main()
    elif action == '2':
        searchAuthors()
        clear()
        main()
    elif action == '3':
        listVenues()
        clear()
        main()
    elif action == '4':
        addArticle()
        clear()
        main()
    else:
        quit()