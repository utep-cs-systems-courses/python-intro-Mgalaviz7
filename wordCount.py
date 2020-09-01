#! /usr/bin/env python3

import re
import os
import sys

# Used retrieve input and output files.
input_file = sys.argv[1]
output_file = sys.argv[2]

# Create a dictionary to hold all words and the number of
# repetitions of the word in the input_file/document.

word_table = {}

# Checks to see if the document that is going to have it words counted exists.

if not os.path.exists(input_file):
    print ("\n"+input_file + " does not exist.\n\nEnter another text file that exists.\n")
    exit()
# Opens the input_file/document and goes line by line replacing all punctuations using a
# regular expression with a blank spave. Followed by lower casing all lines simultaneously
# in the document. Then splits lines up into individual words.

with open (input_file,"r") as in_file:
        for line in in_file:
            file_lines = line.strip()
            words = re.sub(r'[^\w\s]',' ',file_lines)
            words = words.lower()
            word_list = words.split()

            # Goes word by word in the word list and checks if it exists in the dictionary.
            # If the word is not in the dictionary it adds it and gives it a value of 1 to count.
            # If the word exists in the dictionary and has any other value other than None it
            # adds 1 to the count.

            for key in word_list:
                if word_table.get(key) != None:
                    word_count = word_table.get(key) + 1
                    word_table[key] = word_count
                else:
                    word_table[key] = 1
#input_file.close()
                    
# Iterates through the sorted table alphabetically while writing the word and count from
# word_table to the output_file.

last_element_flag = len(word_table)
flag_count = 0

# Creates the file that will output the results of words and the count of repetitions.
new_file = open(output_file , "w")
for word in sorted(word_table.keys()):
    flag_count = flag_count + 1
    word_count = word_table.get(word)

    # Prevents from un-wanted tab at the end of the file.

    if flag_count == last_element_flag:
        new_file.write(word + " " + str(word_count))
    else:
        new_file.write(word + " " + str(word_count) + "\n")
new_file.close()
