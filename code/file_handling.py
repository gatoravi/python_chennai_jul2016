def read_file():
    line_number = 0
    with open("moneyball.csv") as file1:
        for line in file1:
            line_number += 1
            if line_number == 1:
                continue
            fields = line.split("\t")
            if(int(fields[5]) > 20):
                print(fields[5], "wins greater than 20")

read_file()


