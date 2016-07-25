import re

def read_file():
    device_start = False
    with open("moneyball.csv") as file1:
        for line in file1:
            line = line.rstrip("\n")
            if re.match("ATL,NL,2011", line):
                print(line)

read_file()


