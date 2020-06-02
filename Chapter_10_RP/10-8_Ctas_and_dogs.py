# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 202 of the book 'Python crash course' second edition written by Eric MATTHES

def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(contents)

filelist = ['cats.txt', 'dogs.txt']
for file in filelist:
    read_file(file)