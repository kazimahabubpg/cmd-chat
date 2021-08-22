import socket, threading, sys, time

if len(sys.argv) > 1:
	fullUrl = sys.argv[1]
else:
	fullUrl = input("Enter host URL:\033[1;36;40m ")

if fullUrl.startswith("tcp://"):
	fullUrl = fullUrl.replace("tcp://", "")
fullUrl = fullUrl.split(":")

serverUrl = fullUrl[0]
port = int(fullUrl[1])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket initialization
client.connect((serverUrl, port))              #connecting client to server
nickname = input("\033[0;37;40mChoose your nickname: \033[1;33;40m")
print("\033[0;37;40m")

def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            elif (nickname + ":") in message:
            	pass
            else:
                print(message)
        except:                                                 #case on wrong ip/port details
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                 #message layout
        message = '\033[1;33;40m{}: \033[1;36;40m{} \033[1;37;40m'.format(nickname, input('\033[0;37;40m'))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()