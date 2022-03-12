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


## Update One ##
print("Before\n")
for i in mycollection.find():
    print(i)

mycollection.update_one(
    {"name":"IPhone 12 pro"},
    {"$set" : {
        "name" : "IPhone 6s"
    }}
)
print("\After\n")
for i in mycollection.find():
    print(i)


## Update Many ##
print("Before\n")
for i in mycollection.find():
    print(i)

query = {"name":"IPhone 12 pro"}
new_values = {"$set" : {"name":"Samsung Z", "price":14000}}

mycollection.update_many(query, new_values)

print("\After\n")
for i in mycollection.find():
    print(i)