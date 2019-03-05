import socket

"""
HOST = '127.0.0.1'
PORT = 80

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print("1 to exit")

msg = input()
while msg != '1':
    tcp.send(msg)
    msg = input()

print(tcp)
tcp.close()
"""

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

BUFFER_SIZE = 1024
MESSAGE = "Hello!!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
s.close()

print(f'received data: {data}')
