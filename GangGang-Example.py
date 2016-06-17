import GangGang
import sys

## EXAMPLE
def sumdata(data):
    print("I recieved from the client: ", data)
    return sum(data)

if len(sys.argv) < 2:
    print "give 'client' or 'server' as argument"
    exit(0)


host = 'localhost'
port = 9998

if sys.argv[1] == "server":
    GangGang.server(host, port, sumdata)
    print("I returned to the client: ", data)

if sys.argv[1] == "client":
    data = range(10)
    print("I sent to the server: ", data)
    result = GangGang.client(host, port, data)
    print("I recieved from the server: ", result)



