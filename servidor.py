import socket
import sys
import os, time


def conecta_servidor(porta, caminho):
    HOST, PORT = '127.0.0.1', int(porta)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind((HOST, PORT))
    my_socket.listen(5)

    print('Serving on port ', PORT)

    while True:
        connection, address = my_socket.accept()
        request = connection.recv(1024).decode('utf-8')
        string_list = request.split(' ')  # Split request from spaces

        method = string_list[0]
        requesting_file = string_list[1]

        print('Client request ', requesting_file)

        myfile = requesting_file.split('?')[0]  # After the "?" symbol not relevent here
        myfile = myfile.lstrip('/')
        if myfile == '':
            myfile = 'index.html'  # Load index file as default

        try:
            file = open(myfile, 'rb')  # open file , r => read , b => byte format
            response = file.read()
            file.close()

            header = 'HTTP/1.1 200 OK\n'

            if myfile.endswith(".jpg"):
                mimetype = 'image/jpg'
            elif myfile.endswith(".png"):
                mimetype = 'image/png'
            elif myfile.endswith(".txt"):
                mimetype = 'text/txt'
            elif myfile.endswith(".mp3"):
                mimetype = 'music/mp3'
            elif myfile.endswith(".pdf"):
                mimetype = 'text/pdf'
            elif myfile.endswith(".css"):
                mimetype = 'text/css'
            else:
                mimetype = 'text/html'

            header += 'Content-Type: ' + str(mimetype) + '\n\n'
            print(header)

        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode(
                'utf-8')

        timer = time.sleep(20)
        if timer == 0:
            print("Tempo exgot")
            break

        final_response = header.encode('utf-8')
        final_response += response
        connection.send(final_response)
        connection.close()


def child(porta, caminho):
    print('\nA new child ', os.getpid())
    conecta_servidor(porta, caminho)
    os._exit(0)


def parent(porta, caminho):
    while True:
        newpid = os.fork()
        if newpid == 0:
            child(porta, caminho)
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
        reply = input("q for quit / c for new fork")
        if reply == 'c':
            porta = input("Porta para o novo servidor: ")
            continue
        else:
            break


if __name__ == "__main__":
    try:
        caminho = sys.argv[1]
    except:
        print("Não foi adicionado um caminho")
        exit()

    try:
        porta = sys.argv[2]  # porta que será utilizada
    except:
        porta = 8080
    if caminho[len(caminho) - 1] != '/':
        caminho = caminho + '/'

    conecta_servidor(porta, caminho)
    parent(porta, caminho)
