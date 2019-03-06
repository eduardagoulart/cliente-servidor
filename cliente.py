import socket
from trata_dados import ProcessaDadosURL
import re

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
    f = open("request.txt", 'w')
    for i in request:

        f.write(i)
    return request


def retira_cabecalho(request):
    separador = 0
    cabecalho = []

    while '<!DOCTYPE html>' not in request[separador]:
        # cabecalho.append(request[separador])
        # print(cabecalho)
        separador += 1

    corpo = []
    for i in range(0, len(request)):
        if i < separador:
            cabecalho.append(request[i])
        else:
            corpo.append(request[i])

    # corpo = corpo[1:]

    return cabecalho, corpo


if '__main__' == __name__:
    url = 'http://www.viacaopresidente.com.br/portal/'
    host, path = ProcessaDadosURL(url).separa_nome_diretorio()
    reply = http_get(host, path)

    cabecalho, request = retira_cabecalho(reply)

    j = ''
    k = ''
    for i in request:
        if '<!DOCTYPE' in i:

            aux = i.split('\n')[4:]
            print(aux)
            for t in aux:
                k += t
            j +=k
            continue
        j += i

    f = open("cliente.html", 'w')
    f.write(str(j))

    q = ''
    for i in cabecalho:
        q += i

    f = open("cliente.txt", 'w')
    f.write(str(q))

