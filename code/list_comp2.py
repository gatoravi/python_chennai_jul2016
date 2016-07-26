


my_list = [1, 2, 333, 4, 53, 89, 12, 2, 4, 0, -1, 2]

'''
output_list = []

for number in my_list:
    if number > 5:
        output_list.append(number)
'''
print(my_list)

def cube(x):
    return x ** 3

output = list(map(cube, my_list))

print(output)