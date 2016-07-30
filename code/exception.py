import sum

def divide(a, b):
    print(sum_function(a, b))
    A1 = Animal()

def main():
    try:
        divide(10, 3)
        divide(0, 10)
        divide(10, 0)
    except ZeroDivisionError:
        print("divide by zero error")
    divide(10, 1)

main()


