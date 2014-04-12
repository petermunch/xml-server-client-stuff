__author__ = 'munchp'

from xmlrpclib import ServerProxy, MultiCall

server = ServerProxy("http://localhost:8000")
print server
multi = MultiCall(server)
multi.Calculate(2, 100)
multi.pow(2,9)
multi.add(5,1)
multi.add(21,11)
try:
    for response in multi():
        print response
except Error, v:
    print "Error", v