import os # This works with the operating system.
# os.remove("newfile.txt")  # This will delete the specified file, not the file. Will error out if tried twice.
# os.rename("samplefile.txt", "new.txt")  # This renames the file
# Ref 5.3 slideshow for more functions
# os.mkdir("NewDirectory")  # This makes a new directory/folder
# os.rmdir("NewDirectory")  # an error occurs if the directory is not empty
# print(os.getcwd())  # Prints where you are

print("CSV's")
print("Open a CSV by opening new file, then writing .csv at the end")

# try:
#    os.chdir("NewDirectory")  # Can be acessed in the same way as a text file.
#    f = open("newcsv.csv", "r")
#    linesplit = f.readline().split(", ")
#    print(linesplit)
# except:
#    print("Error")

# Task 1: Create a file and then delete it
# os.chdir("NewDirectory")
# f = open("newfile.txt", "x")
# os.remove("newfile.txt")

# Task 2: Create a new directory, put a new file in it, delete the file, and then delete the directory
# os.mkdir("NewestDirectory")
# os.chdir("NewestDirectory")
# open("newfile.txt", "x")
# os.remove("newfile.txt")
# os.remove("NewestDirectory")

# Task 3: Create a csv file (manually) and then read the data from it. Print each item one by one.
# a = open("date.csv", "x")
f = open("date.csv", "r")
print(f.read())

# Task 4: Create a csv file (manually) that has 3 columns: year, month, day.  Read in the data and then for each row
# print the combined data into a date format (ex/ November 22, 2018
# Same as above