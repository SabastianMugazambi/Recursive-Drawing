'''
   recursionExamples.py
   
   Jeff Ondich, 11/1/09
   Trimmed by Jadrian Miles, 2014-05-26
   
   Some simple recursive functions.

   -- In each function, what is (are) the base case(s)?

   -- What happens if you call factorial(100)?  How about fibonacci(100)?
      Why is fibonacci(100) problematic?
      (Don't make these big calls in the pythontutor.com visualizer;
      it'll choke!  Instead just think through why that is.)
'''

def factorial(n):
    print 'Starting factorial(%d)' % (n)
    if n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    print 'Ending factorial(%d) = %d' % (n, result)
    return result

# The Fibonacci numbers are a sequence of integers, where each one is the sum of
# the previous two:
#    0 1 1 2 3 5 8 13 21 34 ...
# This function computes the n-th Fibonacci number, where n starts from 0.  So
# fibonacci(0) returns 0, fibonacci(1) returns 1, fibonacci(2) returns 1, and so
# on.
def fibonacci(n):
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 2) + fibonacci(n - 1)
    return result

def getReversed(s):
    if len(s) == 0:
        return ''
    else:
        return getReversed(s[1:]) + s[0]
