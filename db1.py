import mysql.connector

cnx = mysql.connector.connect(user='yulia1', password='eda1',
                                host='127.0.0.1',
                                database='world_x')
cursor = cnx.cursor()
"""cities = ['Dubai']
for city_name in cities:"""
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


cnx.commit()
cursor.close()
cnx.close()