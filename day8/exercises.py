#Write your code below this line ๐
import math
def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(num_of_cans)} cans of paint.")
#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   

# ๐จ Don't change the code below ๐
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height โ๏ธ wall width) รท coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 โ๏ธ 4) รท 5