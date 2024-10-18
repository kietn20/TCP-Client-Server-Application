import socket

def main():
    # from slide 14 of week 9 TCP slides
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True: # loop to keep the client running
        server_ip = input("Enter server IP address: ")
        server_port = input("Enter server port number: ")

        try:
            server_port = int(server_port)
            server_address = (server_ip, server_port)
        except ValueError:
            print("Error: Please enter a valid integer for port number.")
            continue # restart the loop

        # prompt the user for message
        message = input("Enter message to send (or 'q' to quit program): ")
        if message.lower() == 'q':
            break

        try:
            # send data to server with utf-8 endcoding to destination address (aka server)
            client_socket.sendto(message.encode(), server_address)

            # receive response from server with max buffer size of 1024 bytes
            data, _ = client_socket.recvfrom(1024)

            #print server's response
            print(f"Server response: {data.decode()}") # decode with utf-8

        except socket.gaierror: # error handling for invalid IP address
            print("Error: Invalid IP address. Please enter a valid IP address.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # we have to close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
