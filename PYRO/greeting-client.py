# saved as greeting-client.py
import Pyro4


ns = Pyro4.locateNS()

uri = ns.lookup("example.greeting")

name = "test"
greeting_maker = Pyro4.Proxy(uri)         # get a Pyro proxy to the greeting object
print(greeting_maker.get_fortune(name))   # call method normally

print( greeting_maker.get_numpy_mean(range(100)) )  # call method normally
print( greeting_maker.get_numpy_mean(range(1000)) )   # call method normally

