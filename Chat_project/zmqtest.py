import time
import zmq

# Creating socket
context = zmq.Context()
socket = context.socket(zmq.REP)

# Binding to local adress
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    if message == 'end':
        break
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client with received message
    socket.send_string("Message received!: %s" % message)
