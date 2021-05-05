# Importing necessary libraries
import mysql.connector
import pymongo

# Connecting to MongoDB
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["world_x3"]

# Connecting to MySQL
try:
    cnx = mysql.connector.connect(user='yulia1', password='eda1',
                                  host='127.0.0.1', database='world_x')
except:
    print("I am unable to connect to the database MySQL")
cursorM = cnx.cursor(buffered=True)
cursorM_dict = cnx.cursor(buffered=True, dictionary=True)

# Getting to know tables from MySQL database and make a list of them
cursorM.execute("SHOW TABLES")
x = cursorM.fetchall()
tables = []
for i in x:
    tables.append(i[0])

# ---------------------------------------
# Creating documents in MongoDB
# ---------------------------------------
# Creating first document "city"
# ---------------------------------------
mycol = mydb["city"]

# Deleting documents in MongoDB collection
myquery = {}
mycol.delete_many(myquery)

# Getting information from MySQL
operation = "SELECT * FROM " + tables[0]
cursorM_dict.execute(operation)
city_dict = cursorM_dict.fetchall()

# Creating document in MongoDB
city = city_dict
x = mycol.insert_many(city)

# --------------------------------------
# Creating first document "country"
# ---------------------------------------
mycol = mydb["country"]

# Deleting documents in MongoDB collection
myquery = {}
mycol.delete_many(myquery)

# Getting information from MySQL
operation = "SELECT * FROM " + tables[1]
cursorM_dict.execute(operation)
country_dict = cursorM_dict.fetchall()

# Creating document in MongoDB
country = country_dict
y = mycol.insert_many(country)

# --------------------------------------
# Creating first document "countryinfo"
# ---------------------------------------
mycol = mydb["countryinfo"]

# Deleting documents in MongoDB collection
myquery = {}
mycol.delete_many(myquery)

# Getting information from MySQL
operation = "SELECT * FROM " + tables[2]
cursorM_dict.execute(operation)
countryinfo_dict = cursorM_dict.fetchall()

# Creating document in MongoDB
countryinfo = countryinfo_dict
z = mycol.insert_many(countryinfo)

# --------------------------------------
# Creating first document "countrylanguage"
# ---------------------------------------
mycol = mydb["countrylanguage"]

# Deleting documents in MongoDB collection
myquery = {}
mycol.delete_many(myquery)

# Getting information from MySQL
operation = "SELECT * FROM " + tables[3]
cursorM_dict.execute(operation)
countrylanguage_dict = cursorM_dict.fetchall()

# Creating document in MongoDB
countrylanguage = countrylanguage_dict
a = mycol.insert_many(countrylanguage)




