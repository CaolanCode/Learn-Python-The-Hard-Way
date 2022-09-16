types_of_people = 10
# initialise x and format it with types_of_people variable inside
x = f"There are {types_of_people} types of people"
binary = "binary"
do_not = "don't"
# initialise y and format a string with variables binary and do_not inside
y = f"Those who know {binary} and those who {do_not}"
# print both x and y by itself
print(x)
print(y)
# print formated string with x and y 
print(f"I said: {x}")
print(f"I also said: {y}")
# initial a boolean hilarious
hilarious = False
# initial a variable with curly brackets for formating in the future
joke_evaluation = "Isn't that joke so funny?! {}"
# print joke_evaluation with .format() function to place hilarious boolean 
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "This is the right side."
# concatanate w and e strings
print(w + e)
