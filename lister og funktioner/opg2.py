def add(arg1 : int, arg2 : int, arg3 : int):
    return arg1+arg2+arg3
#print(add(1,2,3))

def str(arg1 : str):
    print(arg1)
#str("hej")

def sum(*args : int):
    result = 1
    for i in args:
        result *= i
    return result
#print(sum(10, 2))

def seks(arg1 : str, arg2 : str, arg3 : int, arg4 : int, arg5 = 1, arg6 = 0):
    print(arg1, arg2, arg3, arg4, arg5, arg6)
#seks("hej", "dav", 3, 4)
