# f = open("demofile.txt", "r")
# r = read, w = write, a = append, r+ = read and write
# print(f.read()) - Reads the whole file
# print(f.readline()) - Reads the first line
# print(f.readline()) - Reads the second line because it does not return to the top
# print(f.readlines())  # Makes a list, \n makes a new line

# f = open("demofile.txt", "a")
# f.write("\nOne more line") - This will keep adding every time it is ran

# f = open("demofile.txt", "w")
# f.write("Ha-ha I just rewrote the entire file.")

# f = open("newfile.txt", "x")

# TASKS:
# 1: Open a file and print the entire contents of it
# 2: Create a file called “November20.txt”.
# 3: Add 3 new lines to your November20.txt file.
# 4: Erase all the contents of November20.txt and write 4 new lines.
# 5: Print out the content of November20.txt line by line.

print("Task 1")
new = open("demofile.txt", "r")
print(new.read())

print("Task 2")
#nov20 = open("November20.txt", "x") - Must be a comment because it was already done
print("Task 3")
nov_20 = open("November20.txt", "a")
nov_20.write("Line 1 \n Line 2 \n Line 3")
nov_20.close()

print("Task 4")
deleting_all = open("November20.txt", "w")
deleting_all.write("Newline 1\nNewline 2\nNewline 3\nNewline 4")
deleting_all.close()  # Closes from writing.

print("Task 5")
list_opening = open("November20.txt", "r")
a = list_opening.readlines()
for x in a:
    print(x, end="") # prints ever other, because print creates a new line, eng negates it


