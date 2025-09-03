from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("8.8.8.8", 80))
serverSocket.listen(1)
while True:
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept()
 try:
  message = connectionSocket.recv(1024).decode()
  filename = message.split()
  f = open(filename[1:], "rb")
  data_respuesta= f.read()
  f.close()
  header = "HTTP/1.1 200 OK\r\n"
  connectionSocket.send(header.encode())
  connectionSocket.send("Content-Type: text/HTML\r\n")
  connectionSocket.send(data_respuesta)
  connectionSocket.close()
 except IOError:
  connectionSocket.send("HTTP/1.1 400".encode())
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data