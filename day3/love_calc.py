print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
total_name = name1 + name2

love_score = 0
love_score += total_name.count("t") * 10
love_score += total_name.count("r") * 10
love_score += total_name.count("u") * 10
love_score += total_name.count("e") * 10
love_score += total_name.count("l") * 1
love_score += total_name.count("o") * 1
love_score += total_name.count("v") * 1
love_score += total_name.count("e") * 1

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")