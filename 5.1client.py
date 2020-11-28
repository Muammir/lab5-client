import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

port = 8888

s.connect(('192.168.56.103', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
