import socket

HOST = ''
PORT = 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print(f'Serving HTTP on PORT {PORT}')

while True:
    cliente_connection, cliente_address = listen_socket.accept()
    request = cliente_connection.recv(1024).decode('utf-8')
    print(f"Request: {request}")

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    string_list = request.split(' ')     # Split request from spaces

    method = string_list[0] # First string is a method
    requesting_file = string_list[1] #Second string is request file

    print('Client request ',requesting_file)

    cliente_connection.close()
    # http_response = str.encode(http_response)
    # cliente_connection.sendall(http_response.encode('utf-8'))
    # cliente_connection.close()

