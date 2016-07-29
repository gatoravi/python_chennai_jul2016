def sum(a = 0, b = 0):
    "This is sum's docstring"
    print("a = ", a, "b = ", b)
    return a + b

print(sum(5, 10))
print(sum(b = 100))
print(sum.__doc__)
