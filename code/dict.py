
employee_salaries = {}

employee_salaries["ravi"] = 10000
employee_salaries["raj"] = 2000
employee_salaries["gokul"] = 5000
employee_salaries["vinod"] = 20000

#print(employee_salaries["vinod"])


for key1 in employee_salaries:
    print("{1}'s salary is {2}".format(key1, employee_salaries[key1]))


"""
with open("moneyball.csv") as moneyball1:
    for line in moneyball1:
        print(line)
"""