import GangGang
import sys

## EXAMPLE
def sumdata(data):
    print("I recieved from the client: ", data)
    return sum(data)

host = 'localhost'
port = 9998

GangGang.server(host, port, sumdata)

