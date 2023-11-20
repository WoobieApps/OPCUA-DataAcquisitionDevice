from .database import send_data_to_database
from .OPC_UA_client import get_data_from_OPC_UA_server
import time
import mysql.connector

def main():
    while True:
        output_data = get_data_from_OPC_UA_server()
        try:
            send_data_to_database(output_data)
            time.sleep(10)
        except mysql.connector.errors.InterfaceError as error:
            print("[DB]: Unable to establish connection to database mysql.agh.edu.pl.")
            time.sleep(1)

if __name__ == '__main__':
    main()