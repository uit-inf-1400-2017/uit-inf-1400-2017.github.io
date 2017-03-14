#!/usr/bin/env python3

"""
This is the t.py code that we worked on during the lecture 2017-03-10. 
"""

def nyttig():
    x = 420
    pass

def foo():
    nyttig()

def hei():
    a = 42
    print(a)
    nyttig()
    foo()

b = 400    
#hei()    


class functracer2:
    """Similar to functracer1, but this one keeps track of call levels for recursive functions"""
    def __init__(self, func):
        self.func = func
        self.level = 0
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.level += 1
        indent = "  " * self.level
        print("{}Entering {} with args {} kwargs {}".format(indent, self.func.__name__, args, kwargs))
        ret = self.func(*args, **kwargs)
        print("{}Returning from {} with return value {}".format(indent, self.func.__name__, ret))
        self.level -= 1
        self.ncalls += 1
        if self.level == 0:
            print("{}Total calls: {}".format(indent, self.ncalls))
            self.ncalls = 0
        return ret

@functracer2
def rec1(i):
    if i > 10:
        return
    print(i)
    rec1(i+1)

#rec1(0)    


@functracer2
def rec_list_maker(i, maxval):
    """Returns a list of values between i and maxval"""
    if i > maxval:
        return []
    newlist = [i] + rec_list_maker(i+1, maxval)
    return newlist


rec_list_maker(3, 6)
