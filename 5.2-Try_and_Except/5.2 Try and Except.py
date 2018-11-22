# new = open("myfile.txt.", "x") - Made into a comment due to the fact that there is an error with it
# try:
# f = open("myfile.txt", "r")
# print(f.read())
# except IOError:  # Certain errors can be picked for specific outomces
#   print("Oh No!")
# except: - Catches everything
# else: - Can be included, if the try is sucessful.

# Task 1: Try to open a file that you do not have and create the file when it errors
try:
    do_not_have = open("unknown.txt", "r")
except IOError:
    print("Hey! you don't have that file.")

# Task 2: Try to find the square root of -1 and then print out “That’s an imaginary number”
# when it doesn’t work using ValueError.
import math
try:
    math.sqrt(-1)
except ValueError:
    print("Thats imaginary!")

# Task 3: Try adding a string to an integer, catch it using ValueError.
string = "trying to add"
try:
    10 + string  # This is a type not a value error.
except TypeError:
    print("You can't do that")

# Task 4: Create a list with 3 things in it, try to access at index 6
# add 3 more things to the list when you catch your error]
listy = ["1", "2", "3"]
try:
    print(listy[5])
except IndexError:
    print("You can't do that!")
