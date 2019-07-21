import zmq

# Prepare our context and sockets
context = zmq.Context()

frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://127.0.0.1:5556")
backend.bind("tcp://127.0.0.1:5555")

#Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

while True:socks = dict(poller.poll())
if socks.get(frontend) == zmq.POLLIN:
    message = frontend.recv_string()
    print('message is here')
    more = frontend.getsockopt(zmq.RCVMORE)
    if more:
        backend.send_string(message, zmq.SNDMORE)
    else:
        backend.send_string(message)

if socks.get(backend) == zmq.POLLIN:
    message = backend.recv_string()
    print('Message is here')
    more = backend.getsockopt(zmq.RCVMORE)
    if more:
        frontend.send_string(message, zmq.SNDMORE)
    else:
        frontend.send_string(message)