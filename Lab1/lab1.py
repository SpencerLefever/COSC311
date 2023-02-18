"""
Spencer Lefever
COSC 311 Lab 1
Text analysis of a research paper
"""
import heapq
import matplotlib.pyplot as plt

#Open file
file = open('SciencePaper.txt', 'r')
word_counts = {}

#Make dictionary for words in file and appearances
for line in file:
    tokens = line.upper().replace(',', ' ').replace(';', ' ').replace('(', ' ').replace(')', ' ').replace('/', ' ')\
    .replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('"', ' ').replace('-', ' ').split()
    for word in tokens:
        try:
            word_counts[word] += 1
        except:
            word_counts[word] = 1


print(len(word_counts), ' number of unique words')
#Find 10 most frequent words
word_lists = {}
for word,count in word_counts.items():
    try:
        word_lists[count].append(word)
    except:
        word_lists[count] = [word]


most_frequent_list = heapq.nlargest(10, word_lists.keys())
most_frequent = {}
print(most_frequent_list)
for count in most_frequent_list:
    most_frequent[count] = word_lists[count]

print(most_frequent)
num_words = 0
print('Most frequent')
for count in most_frequent:
    print(most_frequent[count], ' appeared ', count, '  times')
    num_words += len(most_frequent[count])
    if num_words >= 10:
        break

    
#Find appearance numbers of selected words
print('Selected words frequency')
print('Summerfelt appeared ', word_counts['SUMMERFELT'], ' times')
print('wastewater appeared ', word_counts['WASTEWATER'], ' times')
print('greenhouse appeared ', word_counts['GREENHOUSE'], ' times')
print('salmon appeared ', word_counts['SALMON'], ' times')

#Find Words that appear selected amount of times
print('Selected frequency words')
print('Words that appeared one time: ', word_lists[1])
print('Words that appeared two times: ', word_lists[2])
print('Words that appeared five times: ', word_lists[5])
print('Words that appeared ten times: ', word_lists[10])

#Bar figure for avg length of words per appearance frequency
avg_len = [sum([len(word) for word in value]) / len(value) for value in word_lists.values()]
appearance = list(word_lists.keys())
plt.bar(appearance, avg_len)

file.close()