from pymongo import MongoClient
import json
def addArticle(db):
    """
    Add an article The user should be able to add an article to the collection by providing
    a unique id
    a title
    a list of authors
    and a year. The fields abstract
    and venue should be set to null, references should be set to an empty array and n_citations should be set to zero
    """
    f = open('dblp-ref-1k.json')
    articlesJson = json.load(f)
    
    articles = db["articles"]
    articles.insert_many(articlesJson)

    print("**Add Article**")
    id = input("Enter unique id: ")
    result = db.articles.find({"id":id})
    if result==[]:
        print("id entered not unqiue")
        input("Enter anything to return to the main menu")
        return
    title = input("Enter Title: ")
    authors = input("Enter author(s) separated by spaces").split()
    authors = [author.strip() for author in authors]
    year = input("Enter year: ")
    try:
        db.articles.insertOne({
            "id":id,
            "title": title,
            "authors": authors,
            "year": year,
            "abstract": null,
            "venue": null
        })
    except:
        print("Adding Article failed")
        input("Enter anything to return to the main menu")
        return


if __name__ == "__main__":
    addArticle("27017")