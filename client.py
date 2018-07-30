from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
#s.connect((HOST, PORT)) # connect to server (block until accepted)
s.connect((HOST, 2000)) # connect to server (block until accepted)
s.send('Ola pra vc... ')  # send some data
data = s.recv(1024)     # receive the response
print data              # print the result
s.close()               # close the connection
