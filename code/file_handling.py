def read_file():
    line_number = 0
    with open("moneyball.csv") as filehandle1:
            for line in filehandle1:
                print(line)
                line_number += 1
                if line_number == 10:
                    continue
                fields = line.split(",")
                print(fields)

#read_file()

my_string = "Hello,world"
words = my_string.split(",")
print(words[1])

