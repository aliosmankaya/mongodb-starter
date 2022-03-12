import pymongo

## Local Server ##
## You can connect your local server and use with MongoDB Compass
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

## Cloud Server ##
## You can connect cloud server and use with MongoDB Atlas
myclient = pymongo.MongoClient("mongodb+srv://aliosmank:<password>@cluster0.rwa0g.mongodb.net/node-app?retryWrites=true&w=majority") # Change '<password>' with your db password

## Sample Database and collection
mydb = myclient["node-app"]
mycollection = mydb["products"]


## Find All ##
for i in mycollection.find():
    print(i) 


## Find With Query ##
for i in mycollection.find({},{"_id":0}):
    print(i) 