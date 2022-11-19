from pymongo import MongoClient

def addArticle(port_num):
    """
    Add an article The user should be able to add an article to the collection by providing a unique id, a title, a list of authors, and a year. The fields abstract
    and venue should be set to null, references should be set to an empty array and n_citations should be set to zero
    """

    client = MongoClient('mongodb://localhost:' + port_num)
    db = client['291db']