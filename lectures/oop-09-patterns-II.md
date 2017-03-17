Ch 9 -- Python Design Patterns II
================================

Last time, we discussed Python introducing direct language support for some patterns (such as decorators). 

Consider: Java generics. 

Adapter pattern
----------------

Motivations include:
- existing code where interfaces don't fit and where we cannot easily modify one or both ends.
- provide a common interface to similar classes (example: libraries that provide similar but not identical interfaces)


Adapter, basic use:  wraps around an object so that it can be used by other objects that expect a different interface. 

Book code 1: `DateAgeAdapter` wraps around `AgeCalculator` to allow other date specifications (using `datetime.date` or `datetime.time` objects to specify the date) to be used as `AgeCalculator` only supports dates specified by a string of the format "YYYY-MM-DD". 

Book code 2: The origial `AgeCalculator` objects use `split`. We can also adapt the other way by subclassing `datetime.date` and provide a compatible `split` method on date objects. 

Caution: This only works if the code using the adapted class doesn't change. AgeCalculator could, for instance, do extra checks on the string before trying to parse it, in which case the second adapter would fail. 

Facade pattern
--------------

Similar to Adapter, but tries to simplify a complex interface. Optimizes for a typical or specific usage. 

Flyweight pattern
-----------------

Memory optimization pattern (beware of premature optimizations). 

Basic idea: many similar objects can share attributes/objects for features that are the same between the object. 

One way of implementing: using factory methods that create them when needed, or re-use objects when they already exist (similar to singleton).

Another way: use `__new__` and `weakref`. 


Command pattern
---------------

Basic idea: client code submits code (through a `Command` object) that can later be executed by one or more `Invoker` objects. 

The book demonstrates two ways of implementing this in a menu system:
- A pattern that uses specific method names in objects for specific tasks. This uses three classes of objects and will easily introduce several classes for every action we want to implement.
- A pattern that uses function or method references to implement actions, and requires less class scaffolding. 

The latter (method references) uses a feature in Python where methods are bound to particular objects when you reference them from the object:

```python
# this 
a = obj.method
a()
# is equivalent to
obj.method()
# or
o = obj
o.method()
```

Python threads are provided in a similar fashion, but a closer equivalent to the command pattern is the concurrent library with executors and futures:

https://docs.python.org/dev/library/concurrent.futures.html

Abstract factory pattern
------------------------

Basic idea: a factory that selects the right implementation (based on configuration options, state of the program or other factors) and returns an instance of the selected class. The caller shouldn't need to know which class was actually instanced.

Examples: database implementations, date formatters, compression algorithms.

Book: the right factory is selected based on country code. Could use singleton, but used module variable instead. 


Composite pattern
-----------------

Basic idea: build complex tree-like structures using simple container objects that hold other composite objects. 

Book example: file system folders.

Other typical example: scene graph libraries organize graphics in a hierarchical graph. 
