import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.18.3' # paste your server ip address here
port = 9999
client_socket.connect((host_ip,port)) # a tuple
packet = client_socket.recv(4*1024)
print(packet)
input("end")
client_socket.close()