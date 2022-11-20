from os import system, name
from searchArticle import searchArticle
from searchAuthors import searchAuthors
from listVenues import listVenues
from addArticle import addArticle
from load_json import load_json

def clear(): # clear screen for user
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

port_num = load_json()

def main():



    action = input("Enter\n1 Search for articles\n2 Search for authors\n3 List the venues\n4 Add an article\nAnything else to exit program \n").strip()
    if action=='1':
        searchArticle(port_num)
        clear()
        main()
    elif action == '2':
        searchAuthors(port_num)
        clear()
        main()
    elif action == '3':
        listVenues(port_num)
        clear()
        main()
    elif action == '4':
        addArticle(port_num)
        clear()
        main()
    else:
        quit()

if __name__ == "__main__":
    main()
