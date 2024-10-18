import socket

def main():
    # from slide 15 of week 9 TCP slides
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind the socket to a specific address and port
    server_address = ('localhost', 12345)  # these values can changed as needed
    server_socket.bind(server_address)

    print(f"Server is listening on {server_address[0]}:{server_address[1]}")

    while True: # loop to keep the server running
        # receive data from the client with max buffer size of 1024 bytes
        data, client_address = server_socket.recvfrom(1024)

        # print received message
        print(f"Received message from {client_address}: {data.decode()}")

        # convert the message to uppercase
        message = data.decode().upper()

        # send the uppercase message back to the client
        server_socket.sendto(message.encode(), client_address)

        print(f"Sent uppercase message back to {client_address}")

if __name__ == "__main__":
    main()
