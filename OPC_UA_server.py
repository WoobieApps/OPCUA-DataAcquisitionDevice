from opcua import Server
from random import randint
import datetime
import time

opc_server = Server()

url = "opc.tcp://169.254.123.198:4840"

opc_server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = opc_server.register_namespace(name)

node = opc_server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

opc_server.start()

print(f"Server started at {url}")

while True:
    Temperature = randint(10,50)
    Pressure = randint(200,999)
    TIME = datetime.datetime.now()

    print(Temperature, Pressure, TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)