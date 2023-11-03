#Napisz skrypt (program) w Pythonie tworzący bazę danych.

#Powinien utworzyć bazę danych o nazwie exam2
#Powinien być odporny na błędy połączenia.
#Powinien poinformować użytkownika, jeśli taka baza danych już istnieje.
#Rozwiązanie umieść w pliku answer1.py.
import psycopg2
from psycopg2 import OperationalError
from psycopg2.errors import DuplicateDatabase

CREATE_DB = "CREATE DATABASE exam2;"

try:
    conn = psycopg2.connect(host="localhost" , user="postgres", password ="coderslab")
    conn.autocommit =  True
    cursor = conn.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created.")
    except DuplicateDatabase:
        print("Database exists.")
except OperationalError:
    print("Connection failed!")
else:
    cursor.close()
    conn.close()


try:
    conn = psycopg2.connect(host="localhost", dbname="exam2", user="postgres", password ="coderslab")
    print("Connection successfull.")
    conn.close()
except OperationalError:
    print("Connection failed.")
else:
    cursor.close()
    conn.close()




