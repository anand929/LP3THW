# Introduction to functions
def print_two(*args):
    args1,args2 = args
    print(type(args))
    print(f"arg1: {args1}, arg2: {args2}")


# ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# function with no argument
def print_none():
    print("I got nothing.")


def print_two_args(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


print_two("1","2")
print_two_again("1","2")
print_one("First!")
print_none()
arg = ("1","2")
print_two_args(*arg)
