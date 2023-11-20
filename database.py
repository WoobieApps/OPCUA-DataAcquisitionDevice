import mysql.connector

create_table_query = "CREATE TABLE IF NOT EXISTS data ( id INT AUTO_INCREMENT PRIMARY KEY, \
                                                        variable INT UNSIGNED)"
insert_query = "INSERT INTO data (id, variable) VALUES (%s, %s)"

def send_data_to_database(data_dict):
    # Try connecting to the database
    db = mysql.connector.connect(
        host = "mysql.agh.edu.pl",
        port = 3306, user = "piotrlub", 
        passwd = "maQESXSwFBJJWjbb", 
        database = "piotrlub",
        connect_timeout = 5
    )
    cursor = db.cursor()
    print("[DB]: Connected to database mysql.agh.edu.pl")

    # Create a data table if needed
    cursor.execute(create_table_query)

    for key,value in data_dict.items():
        to_insert = (None,value)
        cursor.execute(insert_query, to_insert)
    
    print("[DB]: New record sent to the database")

    db.commit()
    cursor.close()
    db.close()

    print("[DB]: Disonnected from the database")