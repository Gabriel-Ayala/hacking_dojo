import socket
import datetime
import pandas as pd

HOST = '127.0.0.1'
PORT = 443


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                if ("Dojo" in str(data)):
                    with open('log.txt','a') as log:
                        today  = pd.Timestamp('now')
                        log.write(f''' 
                        [ \n 
                            "log": {data}, \n 
                            "connection": {addr}, \n 
                            "Date": {today.strftime("%d/%m/%Y %H:%M:%S")}, \n
                         ] ,  \n''')