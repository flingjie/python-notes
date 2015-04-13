from functools import wraps
from contextlib import contextmanager
from sys import stdout
from time import time


def timeit(f):
    """ Time something.
    example:
    @timeit
    def doSomething():
        doSomething
    """
    @wraps(f)
    def timed(*args, **kwargs):
        t_start = time()
        result = f(*args, **kwargs)
        t_end = time()

        print '%s took %2.2f sec' % \
                (f.__name__, t_end - t_start)
        return result
    return timed

@contextmanager
def timing(outfile=stdout):
    """ Time something.
    example:
    with timeing() as t:
        doSomething
    """
    t_start = time()
    try:
        yield  
    finally:
        t_end = time()
        outfile.write("cost %2.2f sec\n" % \
                (t_end - t_start))


def extend(class_to_extend):
    """ Extend a Class that already exists.
    example:
    @extend(SomeClassThatAlreadyExists)
    class SomeClassThatAlreadyExists:
        def some_method(self, blahblahblah):
            stuff
            
    example2 extend a method_missing:
    @extend(SomeClassThatAlreadyExists)
    class SomeClassThatAlreadyExists:
        def _missing(*args, **kwargs):
            print "A missing method was called."
            print "The object was %r, the method was %r. " % (self, name)
            print "It was called with %r and %r as arguments" % (args, kwargs)
        return _missing
    """
    @wraps(class_to_extend)
    def decorator(extending_class):
        class_to_extend.__dict__.update(extending_class.__dict__)
        return class_to_extend
    return decorator
