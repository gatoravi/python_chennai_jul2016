def read_file():
    line_number = 0
    with open("moneyball.csv", "r") as filehandle1:
        with open("moneyball_output.tsv", "w") as fh2:
            for line in filehandle1:
                line_number += 1
                if line_number == 1:
                    continue
                fields = line.split(",")
                print(fields)
                fh2.write("\t".join(fields))

read_file()

