import random
# Angela, Ben, Jenny, Michael, Chloe
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
party_size = len(names)
payer = random.randint(0, (party_size - 1))
print(f"{names[payer]} is going to buy the meal today!")