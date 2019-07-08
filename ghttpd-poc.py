import socket

address = ('localhost',80)
strr = "Get "
strr = strr + 'A'*500
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)
client.send(strr)
