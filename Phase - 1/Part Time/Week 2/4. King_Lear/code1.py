import string
from collections import Counter


no_mc_words = 100 

with open('./data/kinglear.txt', 'r') as f:
    data = f.read().replace('\n', ' ')

data = data.translate(str.maketrans('', '', string.punctuation)).lower()
wordcount = Counter(data.split()) 


print("{:<15}{}".format("Word", "Count"))
for item in wordcount.most_common(no_mc_words):
    print("{:<15}{}".format(*item))
