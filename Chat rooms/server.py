import socket
import threading

HOST = '100.88.217.67'  # Accepter les connexions de n'importe quelle adresse
PORT = 64131
LISTENER_LIMIT = 1000  # Augmenter la limite des connexions
clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    username = client.recv(1024).decode()
    if not username:
        client.close()
        return

    clients.append(client)
    broadcast(f"{username} a rejoint le chat\n".encode(), client)

    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(f"{username}: {message.decode()}\n".encode(), client)
        except:
            break

    clients.remove(client)
    client.close()
    broadcast(f"{username} a quitté le chat\n".encode(), None)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(LISTENER_LIMIT)
    print(f"Serveur démarré sur {HOST}:{PORT}")

    while True:
        client, _ = server.accept()
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == '__main__':
    main()
