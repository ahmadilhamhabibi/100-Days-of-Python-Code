import random

name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person = names[random_choice]

print(f"{person}, will pay the meal today")