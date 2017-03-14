#!/usr/bin/env python3
"""
Code that we used to develop the idea of recursion. 
"""


def functracer1(func):
    def wrapper(*args, **kwargs):
        print("Entering {} with args {} kwargs {}".format(func.__name__, args, kwargs))
        ret = func(*args, **kwargs)
        print("  - returned from {} with return value {}".format(func.__name__, ret))
        return ret
    return wrapper

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
def rec_list_maker(i, maxval):
    """Returns a list of values between i and maxval"""
    if i > maxval:
        return []
    if i == maxval:
        return [maxval]
    newlist = [i] + rec_list_maker(i+1, maxval)
    return newlist

def test_rec_list_maker():
    print("Test 1 of rec_list_maker")
    rec_list_maker(3, 5)
    print("Test 2 of rec_list_maker")
    rec_list_maker(3, 10)
#test_rec_list_maker()


def rec_graph_parse1(graph, verbose=True):
    "process items at this level in order" 
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
        elif isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse1(item)

def rec_graph_parse2(graph, verbose=True):
    "process values at this level first, then go deeper" 
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
    for item in graph: 
        if isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse2(item)

def rec_graph_parse3(graph, verbose=True):
    "Go deeper first, then process values at this level" 
    for item in graph: 
        if isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse3(item)
    for item in graph:
        if isinstance(item, int):
            print("** val", item)


simple_graph = [1,2,[3,[4,5],[6,[7]],8],9]

def test_rec():
    # We should kahoot this. 
    for fn in [rec_graph_parse1, rec_graph_parse2, rec_graph_parse3]:
        print("--------------------------")
        print("Recursive graph parsing with", fn.__name__)
        fn(simple_graph)
test_rec()

    
@functracer2
def traced_graph_parser(graph, verbose=True):
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
        elif isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            traced_graph_parser(item)

def test_trace_rec():
    print("--------------------------")
    print("Using the traced graph parser")
    traced_graph_parser(simple_graph)

test_trace_rec()



@functracer2
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    for i in range(7):
        print("-------------------")
        print("Testing fibonacci", i)
        fibonacci(i)
    
test_fibonacci()
