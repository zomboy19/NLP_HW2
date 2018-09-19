# Program to compute bigram probabilities

import csv

from collections import Counter

# Open and read corpus
file = open("corpusA_test.txt", "r")
data = file.read()

#file = open("corpusA.txt", "r")
#data = file.read()

#print(data)

# Convert corpus/sentence into array of words
words = data.split()

#print(words)
#for word in words:
#   print(word)


# No of tokens in corpus
corpus_size = len(words)

print("Corpus size: ",corpus_size)


"""
vocabulary = []
for word in words:
    if not word in vocabulary:
        vocabulary.append(word)

#print(vocabulary)

vocabulary_size = len(vocabulary)
print(vocabulary_size)

#print(vocabulary)

sorted_vocabulary = sorted(vocabulary)
#print(sorted_vocabulary)
"""


wordcount = Counter(words)
#print(wordcount)
print("Vocabulary size: ",len(wordcount))

sorted_wordcount_list = sorted(wordcount)
#print(sorted_wordcount_list)

sorted_wordcount = {}

for word in sorted_wordcount_list:
    sorted_wordcount[word] = wordcount[word]

with open('wordcount.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in sorted_wordcount.items():
        writer.writerow(row)

