import socket

def main():
    host = '127.0.0.1' 
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            key = input("Enter a key to get the value (or 'exit' to quit): ")
            if key.lower() == 'exit':
                break

            client_socket.send(key.encode('utf-8'))
            value = client_socket.recv(1024).decode('utf-8')
            print(f"Value: {value}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()