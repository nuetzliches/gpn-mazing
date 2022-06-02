import socket
import sys

botname = sys.argv[1] # '<Your Username>'

mazeSize = 35 # TODO: x/y
# IPv4
server_address = ('172.16.32.77', 4000)
socketAddressFamily = socket.AF_INET
# IPv6
# server_address = ('gpn-mazing.v6.rocks', 4000) 
# socketAddressFamily = socket.AF_INET6
sock = socket.socket(socketAddressFamily, socket.SOCK_STREAM)

gameEnded = 0
positionX = 0
positionY = 0
goalX = 0
goalY = 0

wallTop = 0
wallRight = 0
wallBottom = 0
wallLeft = 0

initMessage =                                                                                                                                                                                                           'join|' + botname + '|angryWoo)40\n'

def send(msg):
    global sock
    
    print (sys.stderr, 'sending %s' % msg)
    sock.sendall(msg.encode())

def response(data):
    dataSegments = data.split("|")
    print(sys.stderr, 'received "%s"' % dataSegments)

while 1!= 0:

    sock = socket.socket(socketAddressFamily, socket.SOCK_STREAM)
    print (sys.stderr,  'connecting to %s port %s' % server_address)
    sock.connect(server_address)
    try:
        data = sock.recv(800)
        print(sys.stderr, 'received "%s"' % data)

        # Login
        print (sys.stderr, 'sending')
        sock.sendall(initMessage.encode())

        while gameEnded != 1:
            data = sock.recv(80)
            if data == '' or len(data) <= 3:
                break

            print(sys.stderr, 'received "%s"' % data)
            for msg in data.decode().strip().split('\n'):
                response(msg)

    finally:
        print (sys.stderr, 'closing socket')
        sock.close()
