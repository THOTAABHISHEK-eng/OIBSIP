# Chat Client by Abhishek

import socket

def start_client():
    host = "localhost"
    port = 7001

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Connected to Abhishek's Chat Server. Type 'exit' to leave.\n")

    while True:
        msg = input("User: ")
        client.send(msg.encode())

        if msg.lower() == "exit":
            print("You ended the chat.")
            break

        reply = client.recv(1024).decode()
        if not reply:
            print("Server closed connection.")
            break

        print("Abhishek:", reply)

        if reply.lower() == "exit":
            print("Abhishek ended the chat.")
            break

    client.close()

if __name__ == "__main__":
    start_client()