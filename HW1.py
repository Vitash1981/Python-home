import sys # import class sys
import re # import class reg exp
from collections import Counter # import counter
def search_words(textFile: object) -> object:
    text_dict = {} # create new dictionary
    text = re.findall(r'\b\w+[\'\-\w+]\w+\b', textFile.read().lower()) #apply to text reg.exp
    text_dict = Counter(text) #use counter
    for i in sorted(text_dict): #i counter in sorted dict
        print(f'Word is ... "{i}" is placed in text {str(text_dict[i])} time(s) ') # print
if len(sys.argv) < 2:
    with open('/python/Book.txt') as f:
        search_words(f)
else:
    with open(sys.argv[1], 'r') as f:
        search_words(f)
