# Program to compute bigram probabilities
# with and without smoothing

import csv
from collections import Counter

# Open and read corpus
#file = open("corpusA_test.txt", "r")
#data = file.read()

file = open("corpusA.txt", "r")
data = file.read()

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

bigram_list = []
for i in range(len(words)-1):
    bigram_list.append((words[i], words[i+1]))

bigram_count = Counter(bigram_list)
bigram_prob = {}


for bigram in bigram_list:
    #print ("bigram:",bigram)
    #print ("value:",bigram_count.get((bigram)))
    #print ("count of", bigram[0],":")
    #print (sorted_wordcount[bigram[0]])
    bigram_prob[bigram] = ( bigram_count.get(bigram) ) / ( sorted_wordcount[bigram[0]] )

with open('bigram_prob.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in bigram_prob.items():
        writer.writerow(row)

