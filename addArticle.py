from pymongo import MongoClient
import pymongo
def addArticle(db):
    """
    Add an article The user should be able to add an article to the collection by providing
    a unique id
    a title
    a list of authors
    and a year. The fields abstract
    and venue should be set to null, references should be set to an empty array and n_citations should be set to zero
    """

    print("**Add Article**")
    id = input("Enter unique id: ")
    result = db.dblp.find({"id":id})
    for item in result:
        print("id entered not unqiue")
        input("Enter anything to return to the main menu")
        return
    title = input("Enter Title: ")
    authors = input("Enter author(s) separated by spaces: ").split()
    authors = [author.strip() for author in authors]
    year = input("Enter year: ")
    db.dblp.insert_one({
            "id":id,
            "title": title,
            "authors": authors,
            "year": year,
            "abstract": None,
            "venue": None,
            "n_citation": 0
        })
    print("Insert successful")
    return
    '''
    try:
        db.dblp.insertOne({
            "id":id,
            "title": title,
            "authors": authors,
            "year": year,
            "abstract": None,
            "venue": None
        })
    except:
        print("Adding Article failed")
        input("Enter anything to return to the main menu")
        return
    '''



if __name__ == "__main__":
    addArticle("27017")