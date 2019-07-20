import time
import zmq
def history_delete(history_file):
    delete = open(history_file, 'w')
    delete.write('')
    delete.close()
    return 'History deleted'

def show_history(history_file):
    message =''
    file_read = open(history_file,'r')
    for part in file_read.readlines():
        message +='\t'+ part
    file_read.close()
    return message


def make_history(history_file,message):
    file_writer = open('history.txt', 'a+')
    file_writer.write('%s \n' % message)
    file_writer.close()


# Creating socket
context = zmq.Context()
socket = context.socket(zmq.REP)

# Binding to local adress
socket.bind('tcp://127.0.0.1:5555')
history =[]

#file_writer = open('history.txt','a+')
#file_read = open('history.txt','r','UTF-8')


while True:
    #  Wait for next request from client
    message = socket.recv_string()
    if message == 'end':
        print('**********************\n\tClosing server\n**********************')
        break
    elif message == 'history':
        try:
            socket.send_string(show_history('history.txt'))
            print('History :\n%s' % show_history('history.txt'))
        except:
            socket.send_string('No History!')
            print('\n--------------------\n\tNo history!\n--------------------\n')
        continue
    elif message == 'clear':
        socket.send_string(history_delete('history.txt'))
        print('\n--------------------\n \tHistory cleared!\n--------------------\n')
        continue

    print('Received message: %s' % message)
    make_history('history.txt',message)
    #history.insert(len(history)+1,message)
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client with received message
    socket.send_string('Message received!: %s' % message)
