import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["world_x3"]
mycol = mydb["city"]

myquery = { "Name": "Paris" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

myquery = { "Name": "Buenos Aires" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

myquery = { "Name": "Dar es Salaam" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

myquery = { "Name": "Toronto" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

myquery = { "Name": "Kamianske" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)