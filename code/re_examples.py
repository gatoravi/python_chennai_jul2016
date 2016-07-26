import re


def read_coldfusn():
    with open("coldfusn.txt") as fh1:
        for line in fh1:
            line = line.rstrip("\n")
            words = line.split(" ")
            for word in words:
                if re.match("^[1-8]+$", word):
                    print(word)


read_coldfusn()