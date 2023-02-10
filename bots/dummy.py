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
countWins = 0
countLoses = 0

wallTop = 0
wallRight = 0
wallBottom = 0
wallLeft = 0

initMessage =                                                                                                                                                                                                           'join|' + botname + '|angryWoo)40\n'

def send(msg):
    global sock
    
    print ('sending %s\n' % msg)
    sock.sendall(msg.encode())

def response(data):
    global positionX, positionY, goalX, goalY, countWins, countLoses, wallTop, wallRight, wallBottom, wallLeft
    
    dataSegments = data.split("|")
    print('received "%s"' % dataSegments)

    if dataSegments[0] == 'pos':
        if int(dataSegments[1]) < mazeSize:
            positionX = int(dataSegments[1])
        if int(dataSegments[2]) < mazeSize:
            positionY = int(dataSegments[2])
        wallTop = int(dataSegments[3])
        wallRight = int(dataSegments[4])
        wallBottom = int(dataSegments[5])
        wallLeft = int(dataSegments[6])
    elif dataSegments[0] == 'game':
        mazeSize = int(dataSegments[1]) # x
        goalX = int(dataSegments[3])
        goalY = int(dataSegments[4])
    elif dataSegments[0] == 'win' or dataSegments[0] == 'lose':
        countWins = int(dataSegments[1])
        countLoses = int(dataSegments[2])

while 1 != 0:

    sock = socket.socket(socketAddressFamily, socket.SOCK_STREAM)
    print ('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    try:
        data = sock.recv(800)
        print('received "%s"' % data)

        # Login
        print ('sending')
        sock.sendall(initMessage.encode())

        while gameEnded != 1:
            data = sock.recv(80)
            if data == '' or len(data) <= 3:
                break

            print('received "%s"' % data)
            for msg in data.decode().strip().split('\n'):
                response(msg)

                # logic here

            # or here
            # send('move up')
    finally:
        print (sys.stderr, 'closing socket')
        sock.close()
