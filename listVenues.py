from pymongo import MongoClient

def listVenues(port_num): 
    """
    List the venues The user should be able to enter a number n and see a listing of top n venues. For each venue, list the venue, the number of articles in
    that venue, and the number of articles that reference a paper in that venue. Sort the result based on the number of papers that reference the venue with
    the top most cited venues shown first. 
    """
    client = MongoClient('mongodb://localhost:' + port_num)
    db = client['291db']
    quit()