__author__ = 'munchp'

from SimpleXMLRPCServer import SimpleXMLRPCServer

class Calculate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = self.x * self.y

calc = Calculate(10, 10)

print calc.result

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(Calculate)
server.register_function(pow)
server.register_function(lambda x, y: x+y, 'add')
server.register_multicall_functions()
server.serve_forever()
