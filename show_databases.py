import mysql.connector

comandadigital_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="brasil01",

)

meu_cursor = comandadigital_db.cursor()

meu_cursor.execute("SHOW DATABASES")

print(meu_cursor)

for db in meu_cursor:
    print(db)
