import psycopg2

# Connecting to PostreSQL
try:
    conn = psycopg2.connect(dbname='world_x2', user='yulia1',
                            password='eda1', host='localhost')
except:
    print("I am unable to connect to the database Postgre")
cursor = conn.cursor()

cursor.execute("SELECT * FROM city where Name = 'Paris'")
for x in cursor:
    print(x)
cursor.execute("SELECT * FROM city where Name = 'Buenos Aires'")
for x in cursor:
    print(x)
cursor.execute("SELECT * FROM city where Name = 'Dar es Salaam'")
for x in cursor:
    print(x)
cursor.execute("SELECT * FROM city where Name = 'Toronto'")
for x in cursor:
    print(x)
cursor.execute("SELECT * FROM city where Name = 'Kamianske'")
for x in cursor:
    print(x)


# Closing PostgreSQL connection
cursor.close()
conn.close()