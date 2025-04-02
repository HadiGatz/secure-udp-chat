from scapy.all import *

SERVER_IP = '192.168.68.105'
def send_message(message):
    for letter in message:
        port = ord(letter) + 1000
        packet = Ether()/IP(dst=SERVER_IP)/UDP(dport=port)/Raw(load='.')
        sendp(packet)

send_message("hello")



