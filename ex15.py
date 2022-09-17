from sys import argv

script, filename = argv

# opens file
txt = open(filename)

print(f"Here's your file {filename}")
# prints file contents
print(txt.read())
txt.close()

# asks for input of filename from user
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
