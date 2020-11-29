import socket

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.21'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
#    Server = ClientSocket.accept()
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

    filename = input(str("Enter file name to save :"))
    file = open(filename, 'wb')
    file_data = ClientSocket.recv(1024)
    file.write(file_data)
    file.close()
    print('file has been received successfully')

#    filename = input(str("Enter filename of the file :"))
#    file = open(filename, 'rb')
#    file_data = file.read(1024)
#    Server.send(file_data)
#    print("file transferred successfully")

ClientSocket.close()
