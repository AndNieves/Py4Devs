import sqlite3

db = sqlite3.connect('mydb')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, 
                       name TEXT,
                       phone TEXT, 
                       email TEXT unique, 
                       password TEXT)
''')

name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'

cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))

db.commit()

cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone()
print(user1[0])
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
db.close()
