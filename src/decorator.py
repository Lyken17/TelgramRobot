import time


def getTime():
    from datetime import datetime
    return str(datetime.now()).split('.')[0]

class logger(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Entering func : %s(%s %s) at %s" % (self.f.__name__, args, kwargs, getTime()))
        res = self.f(*args, **kwargs)
        print("Exited func : %s(%s %s) at %s" % (self.f.__name__, args, kwargs, getTime()))
        return res


class protect(object):
    def __init__(self, f):
        self.f = f
        self.fp = 'config/robot.json'

    def __call__(self, *args, **kwargs):
        print("protect for \"%s\" start" % self.f.__name__)
        try:
            res = self.f(*args, **kwargs)
        except KeyboardInterrupt:
            print("process interrputed by user at function \"%s\" " % self.f.__name__)
        except IOError:
            print("IO error occurs in function \"%s\" " % self.f.__name__)

        except:
            pass

        print("protect for \"%s\" end" % self.f.__name__)
        return res
