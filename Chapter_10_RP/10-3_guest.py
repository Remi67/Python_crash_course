# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 193 of the book 'Python crash course' second edition written by Eric MATTHES

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("Enter your name: ")
    file_object.write(name + "\n")
