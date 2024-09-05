# Problem 1

for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print('wrong type!')

# Problem 2

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('cannot divide by zero')
finally:
    print('all done')

# Problem 3

def ask():
    while True:
        try:
            res = int(input('please enter a number: '))
        except:
            print('An error has occured try again')
            continue
        else:
            print('Thanks for entering number')
            break
    print(res**2)

ask()