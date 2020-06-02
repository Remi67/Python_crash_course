# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10: try it yourself, page 202 of the book 'Python crash course' second edition written by Eric MATTHES

def ControlNumber():
    print("Press Enter to quit at anytime")
    while True:
        try:
            NumberOne = input("Please enter a first number: ")
            if NumberOne == '':
                break
            NumberOne = int(NumberOne)

            NumberTwo = input("Please enter a second number: ")
            if NumberTwo == '':
                break
            NumberTwo = int(NumberTwo)

        except ValueError:
            print("I need a number")
        else:
            sum = NumberOne + NumberTwo
            print(f"The sum of {NumberOne} and {NumberTwo} gives {sum}")


ControlNumber()