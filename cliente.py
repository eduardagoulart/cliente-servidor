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

    try:
        while '<!DOCTYPE html' not in request[separador]:
            separador += 1

        corpo = []
        for i in range(0, len(request)):
            if i < separador:
                cabecalho.append(request[i])
            else:
                corpo.append(request[i])

        return cabecalho, corpo

    except:
        return "não há cabeçalho"


def nome_sem_diretorio(url):
    try:
        p = url.index('www')
        i = 5
    except:
        i = 0

    nome = []
    while url[i] != '.':
        nome.append(url[i])
        i = i + 1
        if i >= len(url) - 1:
            break

    return ''.join(nome) + '.html'


def nome_com_diretorio(path):
    extensoes = ['.txt', '.mp3', '.pdf', '.html', '.jpg', '.png']
    i = 0
    path = path.split('/')
    while i < len(extensoes):
        if path[len(path) - 1].index(extensoes[i]):
            return path[len(path) - 1]
        i = i + 1
    return "arquivo_generico"


def analisa_erro(response):
    erros = {"302": "302 Found",
             "404": "404 Not Found",
             "301": "301 Moved Permanently",
             "401": "401 Unauthorized",
             "400": "400 Bad Request",
             "403": "403 Forbidden",
             "500": "500 Internal Server Error",
             "504": "504 Gateway Timeout",
             "501": "501 Not Implemented",
             "502": "502 Bad Gateway",
             "503": "503 Service Unavailable"}

    response = response[0].split(" ")
    if response[1] in erros.keys():
        print(erros[response[1]])
        exit(1)


if '__main__' == __name__:
    url = 'http://cenozoicforaminifera.com/sites/cenozoicforaminifera.com/files/styles/slideshow_large/public/Serra-Kiel.jpg?itok=bnHuaBhU'
    host, path = ProcessaDadosURL(url).separa_nome_diretorio()
    reply = http_get(host, path)

    cabecalho, request = retira_cabecalho(reply)

    analisa_erro(cabecalho)
    if len(path) == 0:
        nome_arquivo = nome_sem_diretorio(host)
        arquivo_saida = open(nome_arquivo, 'w')
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
    else:
        nome_arquivo = nome_com_diretorio(path)
        arquivo_saida = open(nome_arquivo, 'w')
        j = request

    arquivo_saida.write(str(j))

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
