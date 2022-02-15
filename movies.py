import sqlite3

												#connection
con = sqlite3.connect("movies.db")
print('Connection Successfully')

# create table

con.execute('''CREATE TABLE movie(
name TEXT,
actor TEXT,
actress TEXT,
yearOfRelease INTEGER)''')
print("Table Created Successfully")


# #insert record
con.execute('''INSERT INTO movie VALUES(
'pushpa', 'Allu Jamval', 'Rasmika Kapoor', 2022);''')
con.commit()
print("Record Inserted Successfully")

#fetch record
cursor=con.execute("SELECT * FROM movie")
print(cursor.fetchall())

# #fetch record with filter
cursor=con.execute("SELECT * FROM movie WHERE actor = 'Vidhyut Jamval'")
print(cursor.fetchall())
