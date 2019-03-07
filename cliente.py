import socket
from trata_dados import ProcessaDadosURL


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
        separador += 1

    corpo = []
    for i in range(0, len(request)):
        if i < separador:
            cabecalho.append(request[i])
        else:
            corpo.append(request[i])

    return cabecalho, corpo


def analisa_erro(response):
    erros = ["302 Found", "502 Bad Gateway", "404 Not Found", "301 Moved Permanently", "401 Unauthorized",
             "400 Bad Request", "403 Forbidden", "500 Internal Server Error", "504 Gateway Timeout",
             "501 Not Implemented", "502 Bad Gateway", "503 Service Unavailable"]


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
            for t in aux:
                k += t
            j += k
            continue
        j += i

    f = open("index.html", 'w')
    f.write(str(j))

    q = ''
    for i in cabecalho:
        q += i
    print(q)
    f = open("cliente.txt", 'w')
    f.write(str(q))
