import GangGang
import sys
import cloudpickle

host = 'localhost'
port = 9998


## EXAMPLE
def sumdata(data):
    print("I recieved from the client: ", data)
    return sum(data)


def sumdata_np(data):
    import numpy as np
    npd = np.array(data)
    print("I recieved from the client: ", npd)
    print np.mean(npd)
    return np.mean(npd)

data = range(10)

func = sumdata_np
print func

print("I sent to the server: ", data)
result = GangGang.cloudpickle_client(host, port, data, func)
print("I recieved from the server: ", result)



