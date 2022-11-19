from pymongo import MongoClient

def searchAuthors(port_num): 
    """
    Search for authors The user should be able to provide a keyword  and see all authors whose names contain the keyword (the matches should be case-
    insensitive). For each author, list the author name and the number of publications. The user should be able to select an author and see the title, year and
    venue of all articles by that author. The result should be sorted based on year with more recent articles shown first.
    """
    client = MongoClient('mongodb://localhost:' + port_num)
    db = client['291db']
    quit()