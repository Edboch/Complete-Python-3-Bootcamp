# check if one.py is being run
# if __name__ == "__main__":
#     RUN THE SCIPRT!
#     function()

def func():
    print("FUNC() in one.py")

print("Top level in one.py")

if __name__ == '__main__':
    print('One.py is being run directly!')
else:
    print('One.py is being imported')