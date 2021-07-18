import socket
from threading import Thread
sock = ''
peers=[]
bind_ip = "localhost"
bind_port = 9999

class Server(object):
    max_connections = 5
    def __init__(self):
        self.setup()
        for i in range(Server.max_connections):
            thread = Server.Connect()
            thread.daemon = True
            thread.start()

    def setup(self):
        global sock
        global bind_ip
        global bind_port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        sock.bind((bind_ip,bind_port,))
        sock.listen(10)

    def send_message(self,message):
        for peer in peers:
            peer.sendall(message)

    class Connect(Thread):
        def run(self):
            peer, addr = sock.accept()
            peers.append(peer)
            while True:
                message = peer.recv(1024)
                print('Response: ' + message.decode())
                for other in peers:
                    if peer != other:
                        other.sendall(message)

server = Server()
try:
    while 1:
        message = input('> ')
        message = message.encode()
        server.send_message(message)
except KeyboardInterrupt:
    sock.close()
    for peer in peers:
        peer.close()
