# NoSQL-MongoDB-Document-Management-System

## User guide
 - Users will be given the choice of entering 1 to search for an article, 2 to search for an author, 3
to list most popular venues, and 4 to add an article
 - If user inputs 1, they will be asked to search multiple keywords to which articles containing those keywords will match and show the results. The user will then have the option to get more information about a certain result.
 - If user inputs 2, they will be asked to search an author’s name to which the articles with a matching author name will come out with results. The user will then have the option to get more information about a certain author.
 - If user inputs 3, they will be asked how many of the most popular venues they’d like to see, and then those venues will be listed.
 - If user inputs 4, they will be asked to enter details required for a new article to be made and an article with those details will be inserted into the database

## Design
We utilized PyMongo to incorporate MongoDB in Python
 - load_json() establish MongoClient, creates collection; read from the json file and insert into the collection
 - listVenues() list the top n venues as the user inputs, the venue name, count of articles and number of articles that reference an article in this venue will be displayed
 - searchArticle() finds articles containing all keywords provided and prints details on them, then more information can be displayed on a certain article and all articles that reference that article searchAuthors() finds amount of articles written by each person from the keyword name and displays short information, and a specific author can be chosen to show all the articles they have written.
