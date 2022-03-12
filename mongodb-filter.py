import pymongo
from bson.objectid import ObjectId


## Local Server ##
## You can connect your local server and use with MongoDB Compass
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

## Cloud Server ##
## You can connect cloud server and use with MongoDB Atlas
myclient = pymongo.MongoClient("mongodb+srv://aliosmank:<password>@cluster0.rwa0g.mongodb.net/node-app?retryWrites=true&w=majority") # Change '<username>' and '<password>' with yours

## Sample Database and collection
mydb = myclient["node-app"]
mycollection = mydb["products"]


## Filter ##
filter = {"name":"IPhone 12 pro"}
result = mycollection.find_one(filter)
print(result)


## Filter One for ID ##
result = mycollection.find_one({"_id":ObjectId("622c888ad960427c59bc4ccc")})
print(result)


## Filter Many ##
result = mycollection.find({
    "name":{
        "$in" : ["IPhone 12 pro", "IPhone 11 pro"]
    }
})

for i in result:
    print(i)


## Filter Comparison ##
result = mycollection.find({
    "price":{
        "$gte":10000 # gte : greater than equal
    }
})

for i in result:
    print(i)


## Filter RegEx ##
result = mycollection.find({
    "name":{
        "$regex":"^I"} # Start with letter 'I'
})

for i in result:
    print(i)