__author__ = 'aramu'

def squared(mylist):
    return [x*x for x in mylist if x > 5]


def negative(mylist):
    return [(x, y) for x in mylist for y in mylist]

def lambda_example(mylist):
    y = map(lambda x: x * x, mylist)
    for square in y:
        print(square)


def len_g_5(mylist):
    return [x for x in mylist if len(x) > 5]



print(squared([1,2,3, 10]))


print(len_g_5(["one", "twowooo", "three", "four"]))