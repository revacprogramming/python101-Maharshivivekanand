
from socket import *

mysock = socket(AF_INET, SOCK_STREAM)
HOST = "www.data.pr4e.org"

cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n".encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()