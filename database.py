import mysql.connector
import time
import random

insert_query = "INSERT INTO data (variable) VALUES (%s)"

while True:
    try:
        db = mysql.connector.connect(
            host = "mysql.agh.edu.pl",
            port = 3306, user = "piotrlub", 
            passwd = "maQESXSwFBJJWjbb", 
            database = "piotrlub",
            connect_timeout = 5
        )
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (variable DOUBLE(7,3))")
        print("Connected")
        value = round(random.uniform(0,1),3)
        cursor.execute(insert_query, (value,))
        db.commit()
        cursor.close()
        db.close()
        time.sleep(60)
    except mysql.connector.errors.InterfaceError as error:
        print(f"Error {error}")
    time.sleep(1)