# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 208 of the book 'Python crash course' second edition written by Eric MATTHES

import json

def get_stored_favnumber():
    """Get stored favoritenumber if available."""
    filename = 'favnumber.json'
    try:
        with open(filename) as f:
            favnumber = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favnumber


def guess_favnumber():
    """Guess the favorite number"""
    favnumber = get_stored_favnumber()
    if favnumber:
        print(f"Your favorite number is, {favnumber}!")
    else:
        favnumber = input("What is your favorite number?")
        filename = 'favnumber.json'
        with open(filename, 'w') as f:
            json.dump(favnumber, f)

guess_favnumber()