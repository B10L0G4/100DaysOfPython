import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random.shuffle(names)

print(names[0])
