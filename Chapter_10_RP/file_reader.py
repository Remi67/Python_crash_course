# Author: Rémi PAUL
# Date: 26-May-2020
# Chapter 10, file reader section of the book 'Python crash course' second edition written by Eric MATTHES


"""
#Reading from a file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
"""
"""
#reading line by Line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
"""

"""
#Making a list fo lines from a file
#Working with a file's contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
"""

"""
#Large files: one million digits
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
"""


#Is your birthday contained Pi?
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first millions digits of pi!")
else:
    print("Your birthday does not appear in the first millions digits of pi.")

