
def read_coldfusn():
    word_count = {}
    line_number = 0
    with open("coldfusn.txt") as fh1:
        for line in fh1:
            words = line.split(" ")
            if "the" in words:
                print("'the' exists")
                print(line)
            else:
                print("'the' doesn't exist")



'''






            for w in words:
                if w in word_count:
                    word_count[w] += 1
                else:
                    word_count[w] = 1

    print("the appears", word_count["the"], " times")
    for word, count in word_count.items():
        if count > 100:
            print(word, count)
'''
read_coldfusn()