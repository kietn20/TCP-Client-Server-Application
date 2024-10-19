import socket

def start_server(host, port):
    # from slide 15 of week 9 TCP slides
    # using with statement to automatically close the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # bind the socket to a specific address and port
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server is listening on {host}:{port}")

        while True:  # main loop to keep the server running
            # wait for a client connection
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")

            try:
                # using with statement to automatically close the client socket
                with client_socket:
                    while True:  # inner loop for receiving messages
                        # Receive data from the client
                        data = client_socket.recv(1024)
                        if not data:
                            break

                        print(f"Received from {client_address}: {data.decode()}")

                        # convert the message to uppercase
                        return_response = data.upper()

                        # send the response back to the client
                        client_socket.send(return_response)

            except Exception as e:
                print(f"Error handling client {client_address}: {e}")
            finally:
                print(f"Connection closed with client: {client_address}")


if __name__ == "__main__":
    host = input("Enter the server IP address: ")
    port = int(input("Enter the server port number: "))
    start_server(host, port)
