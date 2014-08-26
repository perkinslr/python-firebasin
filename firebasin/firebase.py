from dataref import RootDataRef
import urlparse
from connection import Connection

def Firebase(firebaseUrl):
    '''Construct a new Firebase reference from a full Firebase URL.'''

    url = urlparse.urlparse(firebaseUrl)
    root = RootDataRef('https://' + url.netloc)
    if url.path == '/' or url.path == '': 
        return root 
    else:
        return root.child(url.path[1:])


def goOffline():
    for c in Connection.connections:
        c.goOffline()

def goOnline():
    for c in Connection.connections:
        c.goOnline()

Firebase.goOffline = goOffline

Firebase.goOnline = goOnline