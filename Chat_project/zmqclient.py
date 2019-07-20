import zmq
from multiprocessing import Process

# print("Current libzmq version is %s" % zmq.zmq_version())
# print("Current  pyzmq version is %s" % zmq.__version__)


#Auto input loop ip address
def get_ip_address_():
    user_input = (input('Enter ip address to connect to:'))
    if user_input != '':
        usr_input = user_input
    else:
        usr_input = '127.0.0.1'
    return usr_input


'''def send_message():
    while True:
        message = input('Send mesage: ')

        print('Message sent')
        socket.send_string(message)
        if message == 'end':
            print('Closing client!')
            break

def recieve_message():
    message_server = socket.recv_string()
    print('Received reply : \n %s [ %s ]' % (socket_connect_address, message_server))
'''

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)

#get IPv4 address of server
socket_connect_address = get_ip_address_()
print('Connecting to server on %s…' % socket_connect_address)

# Connection to server on ip adress provided by user
socket.connect('tcp://%s:5555' % socket_connect_address)
while True:
    message = input('Send mesage: ')

    print('Message sent')
    socket.send_string(message)
    if message == 'end':
        print('Closing client!')
        break
    elif message == 'history':
        message_server = socket.recv_string()
        print('History: \n%s ' % (message_server))
        continue

    #  Get the reply.
    message_server = socket.recv_string()
    print('Received reply : \n %s [ %s ]' % (socket_connect_address, message_server))
