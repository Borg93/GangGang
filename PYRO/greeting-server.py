# saved as greeting-server.py
import Pyro4
import numpy as np

class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)
    def get_numpy_mean(self, arr):
        return np.mean(arr)

Pyro4.config.HOST = "127.0.0.1"
daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register("example.greeting", uri)

print("Ready.")      # print the uri so we can use it in the client later
daemon.requestLoop()                   # start the event loop of the server to wait for calls

