import socket
import threading

HOST = '100.88.217.67'  # Modifier avec l'IP du serveur si besoin
PORT = 64131

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(message)
        except:
            print("Connexion perdue.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print("Impossible de se connecter au serveur.")
        return

    username = input("Entrez votre pseudo: ")
    client.send(username.encode())

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input()
        if message.lower() == "quit":
            break
        client.send(message.encode())

    client.close()

if __name__ == '__main__':
    main()
