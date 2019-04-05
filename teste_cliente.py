import socket
import sys
import select
from trata_dados import ProcessaDadosURL


def conecta(host, path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    host, path = host.encode(), path.encode()
    print(path)
    s.sendall(b'GET /%b HTTP/1.1\r\nHOST: %b\r\n\r\n' % (path, host))

    reply = b''

    while select.select([s], [], [], 3)[0]:
        data = s.recv(2048)
        if not data:
            break
        reply += data

    headers = reply.split(b'\r\n\r\n')[0]
    image = reply[len(headers) + 4:]

    # save image
    f = open('duda.html', 'wb')
    f.write(image)
    f.close()


if '__main__' == __name__:
    navegador = sys.argv[1]  # vai pegar a opção navegador ou servidor
    url = sys.argv[2]
    try:
        porta = sys.argv[3]  # porta que será utilizada
    except:
        porta = 80

    if navegador == 'navegador':
        host, path = ProcessaDadosURL(url).separa_nome_diretorio()
        conecta(host, path)
    else:
        print("Opção inválida!")
        exit(404)
