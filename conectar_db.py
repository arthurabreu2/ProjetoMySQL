import mysql.connector

comandadigital_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="brasil01",

)

print(comandadigital_db)