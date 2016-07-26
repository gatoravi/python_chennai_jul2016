import nltk
import re
from nltk.corpus import brown


for word in brown.words():
    if re.match("\d*", word):
        print(word)

