import mysql.connector
import psycopg2

# Connecting to MySQL
try:
    cnx = mysql.connector.connect(user='yulia1', password='eda1',
                                  host='127.0.0.1', database='world_x')
except:
    print("I am unable to connect to the database MySQL")
cursorM = cnx.cursor(buffered=True)

# Connecting to PostreSQL
try:
    conn = psycopg2.connect(dbname='world_x2', user='yulia1',
                            password='eda1', host='localhost')
except:
    print("I am unable to connect to the database Postgre")
cursorP = conn.cursor()

# Getting to know tables from database and make a list of them
cursorM.execute("SHOW TABLES")
x = cursorM.fetchall()
tables = []
for i in x:
    tables.append(i[0])
# ---------------------------------------
# Creating tables in PostgreSQL
# ---------------------------------------
# Creating first table - "city"
# ---------------------------------------
# Deleting table in Postgre if exists
operation = "DROP TABLE IF EXISTS " + tables[0]
cursorP.execute(operation)
conn.commit()

# Creating table in Postgre
sql = '''CREATE TABLE ''' + tables[0] + '''(
       ID int not null,
       Name char(35) NOT NULL DEFAULT '',
       CountryCode char(3) NOT NULL DEFAULT '',
       District char(20) NOT NULL DEFAULT '',
       Info json DEFAULT NULL
    );'''
cursorP.execute(sql)
conn.commit()

# Getting information from MySQL
operation = "SELECT * FROM " + tables[0]
cursorM.execute(operation)
city = cursorM.fetchall()

# Inserting it into the first table PostgreSQL
cursorP.executemany("INSERT INTO city VALUES (%s,%s,%s,%s,%s);", city)
conn.commit()

# -------------------------------------
# Creating second table - "country"
# --------------------------------------
# Deleting table in Postgre if exists
operation = "DROP TABLE IF EXISTS " + tables[1]
cursorP.execute(operation)
conn.commit()

# Creating table
sql = '''CREATE TABLE ''' + tables[1] + '''(
       Code char(3) NOT NULL DEFAULT '',
       Name char(52) NOT NULL DEFAULT '',
       Capital int DEFAULT NULL,
       Code2 char(2) NOT NULL DEFAULT ''
    );'''
cursorP.execute(sql)
conn.commit()

# Getting information from MySQL
operation = "SELECT * FROM " + tables[1]
cursorM.execute(operation)
country = cursorM.fetchall()

# Inserting it into the first table PostgreSQL
cursorP.executemany("INSERT INTO country VALUES (%s,%s,%s,%s);", country)
conn.commit()

# -------------------------------------
# Creating third table - "countryinfo"
# --------------------------------------
# Deleting table in Postgre if exists
operation = "DROP TABLE IF EXISTS " + tables[2]
cursorP.execute(operation)
conn.commit()

# Creating table
sql = '''CREATE TABLE ''' + tables[2] + '''(
       doc json DEFAULT NULL,
       _id bytea NOT NULL,
       _json_schema json,
       PRIMARY KEY (_id)
    );'''
cursorP.execute(sql)
conn.commit()

# Getting information from MySQL
operation = "SELECT * FROM " + tables[2]
cursorM.execute(operation)
countryinfo = cursorM.fetchall()

# Inserting it into the first table PostgreSQL
cursorP.executemany("INSERT INTO countryinfo VALUES (%s,%s,%s);", countryinfo)
conn.commit()

# -----------------------------------------
# Creating fourth table - "countrylanguage"
# -----------------------------------------
# Deleting table in Postgre if exists
operation = "DROP TABLE IF EXISTS " + tables[3]
cursorP.execute(operation)
conn.commit()

# Creating table
sql = '''CREATE TABLE ''' + tables[3] + '''(
       CountryCode char(3) NOT NULL DEFAULT '',
       Language char(30) NOT NULL DEFAULT '',
       IsOfficial official NOT NULL DEFAULT 'F',
       Percentage decimal(4,1) NOT NULL DEFAULT '0.0',
       PRIMARY KEY (CountryCode,Language)
    );'''
cursorP.execute(sql)
conn.commit()

# Getting information from MySQL
operation = "SELECT * FROM " + tables[3]
cursorM.execute(operation)
countrylanguage = cursorM.fetchall()

# Inserting it into the first table PostgreSQL
cursorP.executemany("INSERT INTO countrylanguage VALUES (%s,%s,%s,%s);", countrylanguage)
conn.commit()
# ----------------------------------------

# Closing MySQL connection
cursorM.close()
cnx.close()

# Closing PostgreSQL connection
cursorP.close()
conn.close()

