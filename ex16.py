from sys import argv

script, filename = argv

# print a warning to user 
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN.")
input("?")

print("Opening the file...")
target = open(filename, 'w')

# truncating file to empty it's contents
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# input three lines
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

# write each line and a \n character after each
target.write("{}\n{}\n{}\n".format(line1, line2, line3))

# close the file
print("And finally, we close it.")
target.close()
