import pymongo
name = input("Enter your name")
age = int(input("Enter your age"))
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["db"]
collection = mydb["students"]
collection.insert_one({"name" : name, "age": age})
x = collection.find_one()
print(x)