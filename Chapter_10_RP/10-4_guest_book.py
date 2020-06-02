# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 193 of the book 'Python crash course' second edition written by Eric MATTHES

filename = 'guest_book.txt'

with open(filename, "a") as file_object:
    while True:
        guest_input = input("Please enter your name: ")
        if guest_input != '':
            print("Greeting ",guest_input)
            file_object.write(guest_input + " is registered himself.\n")
        else:
            break
