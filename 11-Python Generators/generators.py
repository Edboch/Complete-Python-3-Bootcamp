import random
def gen_squares(n):
    for i in range(n):
        yield i**2

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

s = 'Hello'
iter(s)

# Problem 4
# when there is a large number of numbers that you are counting and do not want to store them all in a list.