import socket, threading                                           

host = '127.0.0.1'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print("Starting chat server on port:\033[1;36;40m ", port, "\033[0;37;40m")
server.listen()

clients = []
nicknames = []

def broadcast(message):                                         
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:                                                         #removing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('\033[1;33;40m{}\033[0;37;40m left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():                                                          #accepting multiple clients
    while True:
        client, address = server.accept()
        print("Connected with \033[1;33;40m{}\033[0;37;40m".format(str(address)))       
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is \033[1;33;40m{}\033[0;37;40m".format(nickname))
        broadcast("\033[1;33;40m{}\033[0;37;40m joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()