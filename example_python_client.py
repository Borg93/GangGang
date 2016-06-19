import GangGang
import sys

host = 'localhost'
port = 9998

data = range(10)

print("I sent to the server: ", data)

result = GangGang.client(host, port, data)

print("I recieved from the server: ", result)
