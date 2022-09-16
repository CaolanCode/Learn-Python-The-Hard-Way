name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
height_cent = height * 2.54
weight = 180 # lbs
weight_kilo = weight * 0.4536
eyes = "Blue"
teeth = "White"
hair = "Brown"


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall or {height_cent} centimetres tall.")
print(f"He's {weight} pounds heavy or {weight_kilo} kilograms")
print("Actually that's not too heavy")
print(f"His teeth are usually {teeth} depending on the coffee")
# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}")

