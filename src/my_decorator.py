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
        # print("protect for \"%s\" start" % self.f.__name__)

        def sysLog(event=""):
            print("======    System Log :    ======\n",
                  "Time : %s\n" % getTime(),
                  "Event : %s\n" % event,
                  "Func : %s(%s %s)" % (self.f.__name__, args, kwargs))

        try:
            res = self.f(*args, **kwargs)
        except KeyboardInterrupt:
            sysLog(event="Interrupted by user")
            exit(-1)
        except IOError:
            sysLog(event="IO error occurred")
        except:
            pass
        # print("protect for \"%s\" end" % self.f.__name__)
        return res
