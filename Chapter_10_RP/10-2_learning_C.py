# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 191 of the book 'Python crash course' second edition written by Eric MATTHES

file_name = 'learning_python.txt'

#Replace the word 'Python' with the word 'C'
with open(file_name) as file_object:
    modified_text = ''
    for line in file_object.readlines():
        modified_text += line.replace('Python', 'C')

print(modified_text)
