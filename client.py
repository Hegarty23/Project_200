import socket
from threading import Thread
nickname=input("Enter your name: ")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipAddress="127.0.0.1"
port=8000
client.connect((ipAddress, port))
print("Connected with server")
def receive():
    while True:
        try:
            message=client.recv(2048).decode("utf-8")
            if message=="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break
def write():
    while True:
        message="{}: {}".format(nickname, input(""))
        client.send(message.encode("utf-8"))
receive_Thread=Thread(target=receive)
receive_Thread.start()
write_Thread=Thread(target=write)
write_Thread.start()