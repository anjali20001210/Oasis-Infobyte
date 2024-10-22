import socket
import threading

# Function to handle client connections (used by the server)
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast messages to all clients (used by the server)
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)
                client.close()

# Function to run the server
def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen(5)
    print("Server started on port 5555...")

    while True:
        client_socket, addr = server.accept()
        print(f"Client connected from {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# Function to handle receiving messages (used by the client)
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("Connection closed by the server.")
            client_socket.close()
            break

# Function to handle sending messages (used by the client)
def send_messages(client_socket):
    while True:
        message = input()
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("Failed to send the message.")
            client_socket.close()
            break

# Function to run the client
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

# Main function to decide whether to run as server or client
if __name__ == "__main__":
    mode = input("Enter 'server' to start the server or 'client' to connect as a client: ").lower()
    clients = []

    if mode == 'server':
        run_server()
    elif mode == 'client':
        run_client()
    else:
        print("Invalid input. Please enter 'server' or 'client'.")
