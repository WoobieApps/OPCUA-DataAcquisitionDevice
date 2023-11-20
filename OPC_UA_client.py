from opcua import Client
import time

url = "opc.tcp://opcua.demo-this.com:51210/UA/SampleServer"

def get_data_from_OPC_UA_server():
    client = Client(url, timeout = 600)
    output_data = dict()

    client.connect()
    print(f"[OPC-UA]: Client connected to: {url}")

    node_dynamic_double = client.get_node("ns=2;i=10848")
    
    print("[OPC-UA]: Client received data")

    output_data["dynamic_double"] = node_dynamic_double.get_value()

    client.disconnect()
    print("[OPC-UA]: Client disconnected")

    return output_data