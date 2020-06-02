# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: Storing data from the book 'Python crash course' second edition written by Eric MATTHES

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
