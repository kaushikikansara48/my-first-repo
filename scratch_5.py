# Server (UDP)
import socket

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(('localhost', 12345))
print('UDP Server listening on port 12345...')

data, addr = udp_server_socket.recvfrom(1024)  # Receive message from client
print(f"Received from {addr}: {data.decode()}")
udp_server_socket.sendto(b'Hello, UDP Client', addr)  # Send response
