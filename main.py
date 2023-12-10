import mysql.connector
import pandas as pd
from opcua import Client
import time


def main():
    while True:
        output_data = get_data_from_OPC_UA_server()
        try:
            send_data_to_database(output_data)
        except mysql.connector.errors.InterfaceError as error:
            print("[DB]: Unable to establish connection to database mysql.agh.edu.pl.")
            time.sleep(1)


create_table_query = "CREATE TABLE IF NOT EXISTS data ( id INT AUTO_INCREMENT PRIMARY KEY, \
                                                        variable INT UNSIGNED)"
insert_query = "INSERT INTO data (id, variable) VALUES (%s, %s)"

opc_ua_url = "opc.tcp://opcua.demo-this.com:51210/UA/SampleServer"


def send_data_to_database(data_dict):
    # Try connecting to the database
    db = mysql.connector.connect(
        host="mysql.agh.edu.pl",
        port=3306,
        user="piotrlub",
        passwd="maQESXSwFBJJWjbb",
        database="piotrlub",
        connect_timeout=5,
    )
    cursor = db.cursor()
    print("[DB]: Connected to database mysql.agh.edu.pl")

    # Create a data table if needed
    cursor.execute(create_table_query)

    for key, value in data_dict.items():
        to_insert = (None, value)
        cursor.execute(insert_query, to_insert)

    print("[DB]: New record sent to the database")

    db.commit()
    cursor.close()
    db.close()

    print("[DB]: Disonnected from the database")


def get_data_from_OPC_UA_server():
    client = Client(opc_ua_url, timeout=600)
    output_data = dict()

    client.connect()
    print(f"[OPC-UA]: Client connected to: {opc_ua_url}")

    node_dynamic_double = client.get_node("ns=2;i=10848")

    print("[OPC-UA]: Client received data")

    output_data["dynamic_double"] = node_dynamic_double.get_value()

    client.disconnect()
    print("[OPC-UA]: Client disconnected")

    return output_data


if __name__ == "__main__":
    main()
