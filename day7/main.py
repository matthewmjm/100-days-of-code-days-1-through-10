import random
#Step 1 
word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
size = len(word_list)
word_chose = random.randint(0, (size - 1))
chosen_word = word_list[word_chose]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
guess_length = len(chosen_word)
i = 0
while i < guess_length:
    if guess == chosen_word[i]:
        print("Right")
    else:
        print("Wrong")
    i += 1
