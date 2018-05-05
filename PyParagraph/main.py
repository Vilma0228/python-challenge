import os
import string
import re

#Files to read & variables
file = open("paragraph_1.txt")
text = file.read()

#Count using split function

words = text.split(" ")
sentences = re.split("(?<=[.!?]) +", text)

    #print (words)
    #print (sentences)

word_counts = len(words)
sentence_counts = len(sentences)

#Compute for Average 
average_words = word_counts/sentence_counts

#Solve for total of all letter counts

validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterCount = {}
letterCount.update([(x,0) for x in validLetters])

with open("paragraph_1.txt", "r") as file:
    for letter in file.read():
        if letter in validLetters:
            letterCount[letter] += 1

    #print(letterCount)

total_letters =sum(letterCount.values())

    #print(total_letters)

#Solve for average total letter count / word count
average_letter_count = (total_letters/word_counts)

print ("Approximate Word Count:", word_counts)
print ("Approximate Sentences:", sentence_counts)
print ("Average Letter Count in Words:", average_letter_count)
print ("Average Sentence Length in Words:", average_words)

