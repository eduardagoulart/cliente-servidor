import socket
from trata_dados import ProcessaDadosURL

"""
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
# HTTP/1.1 200 OK

# Hello, World!
"""
    string_list = request.split(' ')     # Split request from spaces

    method = string_list[0] # First string is a method
    requesting_file = string_list[1] #Second string is request file

    print('Client request ',requesting_file)

    cliente_connection.close()
    # http_response = str.encode(http_response)
    # cliente_connection.sendall(http_response.encode('utf-8'))
    # cliente_connection.close()
"""


def http_get(host, path):
    request = []
    print(f'Host: {host}, type: {type(host)}')
    print(f'path: {path}, type: {type(path)}')
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            request.append(str(data, 'utf-8'))
        else:
            break
    s.close()
    return request


if '__main__' == __name__:
    url = 'http://www.viacaopresidente.com.br/portal/'
    host, path = ProcessaDadosURL(url).separa_nome_diretorio()
    reply = http_get(host, path)

    j = ''
    for i in reply:
        j += i

    f = open("cliente.html", 'w')
    f.write(str(j))
