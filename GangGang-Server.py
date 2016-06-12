import socket
import pickle
import time
import numpy as np

def recv_timeout(the_socket , timeout=1):
    the_socket.setblocking(0)
     
    total_data=[]
    data=''
     
    begin = time.time()

    while True:
        #if you got some data, then break after timeout
        if total_data and time.time() - begin > timeout:
            break
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time() - begin > timeout * 2:
            break
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
    #join all parts to make final string
    return ''.join(total_data)

def recv_unpickle(socket, callback):
    data = recv_timeout(conn)
    if len(data) > 0:
        try:
            callback( pickle.loads(data) , socket)
        except EOFError, e:
            return None


def process_data(data, socket):
    print "RECEIVED!:"

    time.sleep(0.5)

    print " "
    print "TURNING INTO NUMPY ARRAY:"
    npd = np.array(data)
    print npd

    if type(data).__name__ == 'list':
        result = np.sum(npd)

    time.sleep(0.5)

    print " "
    print "the total is:", result
    
    time.sleep(0.5)
    
    print "SENDING: ", result
        
    socket.sendall(str(result))


############

if __name__ == "__main__":

    host = '172.16.15.1'
    port = 9090

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, port))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    while True:
        conn, addr = serversocket.accept()
        recv_unpickle(conn, process_data)

