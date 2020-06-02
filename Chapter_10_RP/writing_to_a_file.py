# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10, writing to a file section of the book 'Python crash course' second edition written by Eric MATTHES

"""
#Writing multiple lines
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
"""

#Appending to a File
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")