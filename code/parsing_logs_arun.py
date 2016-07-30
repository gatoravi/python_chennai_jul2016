import re

def check_patterns():
    patterns_list = []

    #Read patterns file
    with open("patterns.txt") as patterns1:
        for line in patterns1:
            line = line.rstrip("\n")
            patterns_list.append(line)
        print(patterns_list)

    #Read log file
    with open("Sample Logs.txt") as log1:
        with open("matching_logs.txt", "w") as output_fh:
            for log_line in log1:
                log_line = log_line.rstrip("\n")
                for pattern in patterns_list:
                    match = re.search(pattern, log_line)
                    if match != None:
                        log_line.lstrip(" ")
                        count = int(match.group(1))
                        host = match.group(2)
                        if count > 100:
                            print(host, " Has count > 100")
                            print(log_line)




def rstrip_example():
    s1 = "hello"
    s1 = s1.rstrip("lo")
    print(s1)

check_patterns()