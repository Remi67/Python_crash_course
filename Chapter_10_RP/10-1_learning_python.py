# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 191 of the book 'Python crash course' second edition written by Eric MATTHES

file_name = 'learning_python.txt'

#print the contents once by reading the entire file
with open(file_name) as file_object:
    file_string = file_object.read()
    print(file_string)

#print the contents once by looping over the file object
with open(file_name) as file_object:
    for line in file_object.readlines():
        print(line.rstrip())

#print the contents once by storing the file in a list
with open(file_name) as file_object:
    string = '\n'
    for line in file_object.readlines():
        string += line
    print(string)

