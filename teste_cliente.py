import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# http:///
s.connect(('cenozoicforaminifera.com', 80))
s.sendall(b'GET /sites/cenozoicforaminifera.com/files/styles/slideshow_large/public/Serra-Kiel.jpg?itok=bnHuaBhU HTTP/1.1\r\nHOST: cenozoicforaminifera.com\r\n\r\n')

reply = b''

while select.select([s], [], [], 3)[0]:
    data = s.recv(2048)
    if not data: break
    reply += data

headers =  reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]

# save image
f = open('image.jpg', 'wb')
f.write(image)
f.close()