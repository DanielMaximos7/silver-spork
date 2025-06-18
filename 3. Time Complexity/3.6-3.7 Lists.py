#3.6 Lists...

#making a list 4 different ways:

def test1():
    l = []
    for i in range(1000):
        l = l + [i]  # Concatenating a list with a single element

def test2():
    l = []
    for i in range(1000):
        l.append(i) # Appending a single element to a list
    
def test3():
    l = [i for i in range(1000)] # List comprehension

def test4():
    l = list(range(1000)) # Built-in function

#create a timer for each of the functions

from timeit import Timer
"""
 In this case the statement from __main__ import test1 imports the function test1 from the __main__ namespace into the namespace that timeit sets up for the timing experiment. 
 The timeit module does this because it wants to run the timing tests in an environment that is uncluttered by any stray variables you may have created, 
 that may interfere with your function’s performance in some unforeseen way.
"""

t1 = Timer("test1()", "from __main__ import test1")
#print("concat",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
#print("append",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
#print("comprehension",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
#print("list range",t4.timeit(number=1000), "milliseconds")

#comparing the contains operation between lists and dictionaires.

#We will confirm that the contains operator for lists is O(n)
#and the contains operator for dictionaries is O(1)


import timeit
import random

for i in range(10000, 100001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")

    x = list(range(i))  # Create a list of numbers from 0 to i-1

    lst_time = t.timeit(number=1000)  # Time the contains operation for the list

    x = {j: None for j in range(i)}  # Create a dictionary with keys from 0 to i-1

    d_time = t.timeit(number=1000)  # Time the contains operation for the dictionary

    print("%d: %f seconds for list, %f seconds for dictionary" % (i, lst_time, d_time))