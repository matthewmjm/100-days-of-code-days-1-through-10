total = 0
for number in range (1, 101):
    if number % 2 == 0:
        total += number
    else:
        total = total
print(f"The total of even numbers from 1 through 100 is: {total}")