# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: Storing data from the book 'Python crash course' second edition written by Eric MATTHES

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
