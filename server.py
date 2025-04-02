import socket
from threading import Thread

def listening_to_port(port_number):
    listener = socket.socket()
    listener.bind(('', port_number))
    listener.listen()
    client, addr = listener.accept()
    print(chr(port_number))

port_listener = Thread(target=listening_to_port, args=(1032,))
for i in range(1097, 1122):
    port_listener = Thread(target=listening_to_port, args=(i,))
    port_listener.start()