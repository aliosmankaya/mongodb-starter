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


## Insert One ##
product = {"name":"IPhone 12pro", "price":15000}

result = mycollection.insert_one(product)

print(result)
print(type(result))
print(result.inserted_id)


## Insert Many ##
productList = [
    {"name":"IPhone 12 pro", "price":15000, "description":"256GB"},
    {"name":"IPhone 11 pro", "price":12000, "categories":["phone", "electronic"]},
]

result = mycollection.insert_many(productList)

print(result)
print(type(result))
print(result.inserted_ids)