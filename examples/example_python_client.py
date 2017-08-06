import GangGang

host = 'localhost'
port = 9998

data = range(100)

print("I sent to the server: ", data)

result = GangGang.client(host, port, data)

print("I recieved from the server: ", result)
