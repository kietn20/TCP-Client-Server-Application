import socket

def main():
    while True:  # main loop to keep the client running
        server_ip = input("Enter server IP address: ")
        server_port = input("Enter server port number: ")

        try:
            server_port = int(server_port)

            # from slide 14 of week 9 TCP slides
            # using with statement to automatically close the socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((server_ip, server_port))
                print(f"Connected to server at {server_ip}:{server_port}")

                while True:  # inner loop for sending messages
                    message = input("Enter message to send (or 'q' to quit): ")
                    if message.lower() == 'q':
                        break

                    # send data to server with utf-8 endcoding to destination address (aka server)
                    client_socket.sendall(message.encode())

                    # receive response from server with max buffer size of 1024 bytes
                    data = client_socket.recv(1024)

                    # print server's response
                    # decode with utf-8
                    print(f"Server response: {data.decode()}")

                print("Disconnected from server.")
                break  # exit the main loop after disconnecting

        except ValueError:
            print("Error: Please enter a valid integer for port number.")
        except socket.gaierror:
            print("Error: Invalid IP address. Please enter a valid IP address.")
        except ConnectionRefusedError:
            print(
                "Error: Connection refused. Make sure the server is running and the IP and port are correct.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
