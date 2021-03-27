row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
x = int(int(position)/10)
y = int(position) - (x * 10)
map[y - 1][ x - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
