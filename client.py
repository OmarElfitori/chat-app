import socket
import threading

HOST = input("Enter server IP: ")
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NAME":
                client.send(name.encode())
            else:
                print(message)

        except:
            print("Disconnected.")
            client.close()
            break


def write():
    while True:
        message = f"{name}: {input('')}"
        client.send(message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()