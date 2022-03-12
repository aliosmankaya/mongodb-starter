import pymongo


## Local Server ##
## You can connect your local server and use with MongoDB Compass
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

## Cloud Server ##
## You can connect cloud server and use with MongoDB Atlas
myclient = pymongo.MongoClient("mongodb+srv://aliosmank:<password>@cluster0.rwa0g.mongodb.net/node-app?retryWrites=true&w=majority") # Change '<username>' and '<password>' with yours

## Sample Database and collection
mydb = myclient["node-app"]
mycollection = mydb["products"]


## Sort ##
result = mycollection.find().sort("name", -1) # Sort for 'name' descending

result = mycollection.find().sort("price") # Sort for 'price' ascending

result = mycollection.find().sort([("name",1), ("price",-1)]) # Sort for 'name' ascending and 'price' descending

for i in result:
    print(i)