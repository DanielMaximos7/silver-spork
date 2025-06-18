#3.1.1 Programming Exercises

#devise an expirement to verify that the list index operator is O(1)

def test_list_index():
    l = list(range(100000))  # Create a list with 100,000 elements
    index = 99999  # Index to access the last element
    return l[index]  # Access the element at the specified index

# Timing the list index operation
from timeit import Timer
t = Timer("test_list_index()", "from __main__ import test_list_index")
print("Time taken for list index operation:", t.timeit(number=1000), "milliseconds")


