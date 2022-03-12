import pymongo


## Local Server ##
## You can connect your local server and use with MongoDB Compass
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

## Cloud Server ##
## You can connect cloud server and use with MongoDB Atlas
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.rwa0g.mongodb.net/node-app?retryWrites=true&w=majority") # Change '<username>' and '<password>' with yours

## Sample Database and collection
mydb = myclient["node-app"]
mycollection = mydb["products"]


## Delete One ##
print("Before\n")
for i in mycollection.find():
    print(i)

mycollection.delete_one({"name":"IPhone 6s"})

print("\nAfter\n")
for i in mycollection.find():
    print(i)


## Delete Many ##
print("Before\n")
for i in mycollection.find():
    print(i)

mycollection.delete_many({"name":"Samsung Z"})

print("\nAfter\n")
for i in mycollection.find():
    print(i)