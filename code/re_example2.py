import re
#http://regexone.com/lesson/letters_and_digits

my_test_string = ".Thee world was better in 1990. Jai Hind!"

pattern1 = "^.*better in (.*)\. (\w+) (.*)(\W)$"
result = re.match(pattern1, my_test_string)
if result:
    print("Matches")
    #print(result.group(1), result.group(2), "group3:", result.group(3), "group4:", result.group(4))
    print(result.group(1, 2, 3, 4))
else:
    print("Doesn't match")

