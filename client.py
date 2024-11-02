import socket
from threading import Thread

nickname = input("Enter your nickname ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 8000
client.connect((ip,port))

def recieve():
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message == 'NICKNAME':
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break
def write():
    while True:
        message = '{}:{}'.format("nickname",input(''))
        client.send(message.encode("utf-8"))

recieve_thread = Thread(target=recieve)
recieve_thread.start()
write_thread = Thread(target=recieve)
write_thread.start()