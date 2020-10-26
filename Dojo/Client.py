import socket

HOST = '127.0.0.1'
PORT = 443
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket:
    
    msg = input('Write a mensage: ')

    socket.connect((HOST,PORT))
    socket.sendall(msg.encode('utf-8'))