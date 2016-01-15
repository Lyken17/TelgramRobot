import time


def getTime():
    from datetime import datetime
    return str(datetime.now()).split('.')[0]

class logger(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Entering func : %s(%s %s) at %s"  % (self.f.__name__, args, kwargs, getTime() ))
        res = self.f(*args, **kwargs)
        print("Exited func : %s(%s %s) at %s"  % (self.f.__name__, args, kwargs, getTime() ))
        return res

class protect(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("protect start")
        res = self.f(*args, **kwargs)
        print("protect end")
        return res