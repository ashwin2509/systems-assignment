import socket
import sys 


def load_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
        	splitted_values = line.split(' ')
        	key = splitted_values[0]
        	values = ' '.join(splitted_values[1:])
        	data[key] = values
    return data


def handle_client(client_socket, data):
    while True:
        query = client_socket.recv(1024).decode('utf-8')
        if not query:
            break

        value = data.get(query, "Key not found")

        client_socket.send(value.encode('utf-8'))

    client_socket.close()


def main():
	path = sys.argv[1]
	host = "127.0.0.1" 
	port = 12345  

	data = load_data(path)

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen(5)
	print(f"Server listening on {host}:{port}")

	try:
	    while True:
	        client_socket, addr = server_socket.accept()
	        print(f"Accepted connection from {addr[0]}:{addr[1]}")
	        handle_client(client_socket, data)
	except KeyboardInterrupt:
	    print("Server shutting down...")
	finally:
	    server_socket.close()



if __name__ == "__main__":
	main()
