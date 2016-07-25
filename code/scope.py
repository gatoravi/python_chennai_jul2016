a = 20

def my_function1():
    print("inside func1")
    a = 30
    print(a)

def my_function2():
    print("inside func2")
    print(a)

my_function1() #functioncall
print("outside")
print(a)
my_function2()