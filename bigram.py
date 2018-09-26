# Program to compute bigram probabilities
# with and without smoothing

import csv
from collections import Counter

def DictToFile(DictToWrite,Filename):
    """This function writes data from a dictionary to a CSV file
    Args:
        DictToWrite: A dictionary that need to be written to the file
        Filename: A name to give to the file.
    """
    CSVFile = Filename+'.csv'
    with open(CSVFile, 'w', newline = '') as f:
        writer = csv.writer(f)
        for row in DictToWrite.items():
            writer.writerow(row)


#file = open("corpusA_test.txt", "r")
#data = file.read()                              # Get corpus data
file = open("corpusA.txt", "r")
data = file.read()


words = data.split()                            # Convert corpus/sentence into array of words
corpus_size = len(words)                        # No of tokens in corpus / Corpus size
print("Corpus size: ",corpus_size)
wordcount = Counter(words)                      # Get histogram of all words 
print("Vocabulary size: ",len(wordcount))       # Vocabulary size
sorted_wordcount_list = sorted(wordcount)       # Sort wordcount to make search easier


sorted_wordcount = {}                           # Get sorted wordcount in this dictionary
for word in sorted_wordcount_list:
    sorted_wordcount[word] = wordcount[word]


DictToFile(sorted_wordcount,"Wordcount")        # Get wordcount in a file named "Wordcount"


bigram_list = []                                # Generate a list of all bi-grams from the corpus text 
for i in range(len(words)-1):                   # Iterate over corpus and keep storing all bi-grams in a list
    bigram_list.append((words[i], words[i+1]))  # Bi-gram = (this word, next word)

print("Total number of bi-grams: ",len(bigram_list))

bigram_count = Counter(bigram_list)             # Get histogram of all bi-grams

unique_bigram_list = sorted(list(set(bigram_list)))
print("Number of unique bi-grams: ",len(unique_bigram_list))


bigram_prob = {}
for bigram in unique_bigram_list:
    #print ("bigram:",bigram)
    #print ("value:",bigram_count.get((bigram)))
    #print ("count of", bigram[0],":")
    #print (sorted_wordcount[bigram[0]])
    bigram_prob[bigram] = ( bigram_count.get(bigram) ) / ( sorted_wordcount[bigram[0]] )

DictToFile(bigram_prob,"Bigram Probabilities")