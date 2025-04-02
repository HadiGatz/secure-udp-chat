from scapy.all import *

SERVER_IP = '127.0.0.1'
def send_message(message):
    for letter in message:
        port = ord(letter) + 1000
        packet = Ether()/IP(dst=SERVER_IP)/UDP(dport=port)
        send(packet)

send_message("hello")



