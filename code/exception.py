__author__ = 'aramu'


def main():
    my_list_of_pairs = [(1, 3), (20, 5), (1, "100"), (1, 2)]
    for num1, num2 in my_list_of_pairs:
        try:
            print(num1 + num2)
            #raise TypeError("This is my exception!")
        except TypeError as e1:
            print("Unable to add, mixed types!")
            print(e1)
        else:
            print("in else block")

main()

