import zmq

def get_ip_address_():
    user_input = (input("Enter ip adress to connect to:"))
    if user_input != '':
        usr_input = user_input
    else:
        usr_input = '127.0.0.1'
    return usr_input

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)

socket_connect_address = get_ip_address_()
print("Connecting to server on %s…" % socket_connect_address)

# Connection to server on ip adress provided by user
socket.connect("tcp://%s:5555" % socket_connect_address)

# print("Current libzmq version is %s" % zmq.zmq_version())
# print("Current  pyzmq version is %s" % zmq.__version__)


#  Do 10 requests, waiting each time for a
while True:
    message = input("Send mesage: ")

    print("Message sent")
    socket.send_string(message)
    if message == 'end':
        break

    #  Get the reply.
    message_server = socket.recv_string()
    print("Received reply %s [ %s ]" % (socket_connect_address, message_server))
