# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: Storing data from the book 'Python crash course' second edition written by Eric MATTHES

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
