# example of the usage of doctests

def fib(n): # sample function
    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    55
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

import doctest # importing the function

if __name__ == "__main__": # confirm that the file is being ran as a standalone
    doctest.testmod(verbose = True) # run the test