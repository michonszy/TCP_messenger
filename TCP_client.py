import socket
from threading import Thread

target_host = 'localhost'
target_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target_host, target_host,))

class WatchForReply(Thread):
    def run(self):
        while True:
            reply = sock.recv(1024)
            print('Response: ' + reply.decode())

thread = WatchForReply()
thread.daemon = True
thread.start()

while True:
    message = input('> ')
    message=message.encode()
    sock.sendall(message)
