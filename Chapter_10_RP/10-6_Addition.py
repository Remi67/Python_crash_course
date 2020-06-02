# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 201 of the book 'Python crash course' second edition written by Eric MATTHES

def ControlNumber():
        try:
            NumberOne = input("Please enter a first number: ")
            NumberOne = int(NumberOne)

            NumberTwo = input("Please enter a second number: ")
            NumberTwo = int(NumberTwo)
        except ValueError:
            print("I need a number")
        else:
            sum = NumberOne + NumberTwo
            print(f"The sum of {NumberOne} and {NumberTwo} gives {sum}")


ControlNumber()
