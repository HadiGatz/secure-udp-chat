import socket
from threading import Thread

def listening_to_port(port_number):
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.bind(('', port_number))
    while True:
        data, addr = listener.recvfrom(1024)  
        print(chr(port_number - 1000), end='')

listeners = []
space_listener = Thread(target=listening_to_port, args=(1032,))
space_listener.start()
listeners.append(space_listener)
for i in range(1097, 1122):
    port_listener = Thread(target=listening_to_port, args=(i,))
    port_listener.start()
    listeners.append(port_listener)