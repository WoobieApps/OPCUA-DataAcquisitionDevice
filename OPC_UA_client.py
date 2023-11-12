from opcua import Client
import time

def (connect)
url = "opc.tcp://opcua.demo-this.com:51210/UA/SampleServer"

client = Client(url, timeout = 600)

client.set_encoding_limits(
    max_string_length=16384,
    max_array_length=16384,
    max_byte_string_length=16384,
    max_message_size=16777216,
)

client.connect()
print("Client connected")


node_val = client.get_node("ns=2;i=10854")
val = node_val.get_value()
print(val)
