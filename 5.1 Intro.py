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

f = open("newfile.txt", "x")
