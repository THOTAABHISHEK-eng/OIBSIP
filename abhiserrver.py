# Chat Server by Abhishek

import socket

def start_server():
    host = "localhost"
    port = 7001

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Abhishek's Chat Server started. Waiting for connection...")

    conn, addr = server.accept()
    print("Connected with", addr)

    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            print("Client disconnected.")
            break

        if msg.lower() == "exit":
            print("Chat ended by Client (User).")
            break

        print("User:", msg)
        reply = input("Abhishek: ")
        conn.send(reply.encode())

        if reply.lower() == "exit":
            print("Chat ended by Abhishek.")
            break

    conn.close()
    server.close()

if __name__ == "__main__":
    start_server()