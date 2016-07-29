import shutil
import re

def write_10less():
    line_number = 0
    with open("moneyball.csv") as fh1:
        with open("~/Desktop/moneyball_10less.csv", "w") as fh2:
            for line in fh1:
                line_number += 1
                if re.match("#", line):
                    continue
                fh2.write(line)
        with open("~/Desktop/moneyball_10less.csv", "w") as fh2:
            fh2.write("Hello")
    shutil.move("~/Desktop/moneyball_10less.csv", "moneyball.csv")
    shutil.

write_10less()