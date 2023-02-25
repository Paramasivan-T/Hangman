import random
from hangman_art import stages, logo
from hangman_words import word_list

# TO choose a word from the list and get input
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives = 6
print(chosen_word)
print(logo)

# Display the blank lines
display = []
for _ in range(word_length):
    display += "_"
print(display)

# Repeat the code until the game is over
while not game_over:
    # To get a letter a a input
    guess = input("Guess a letter: ")

    if guess in display:
        print("You Already gussed the letter")

    # To check the condtion whether the gussed letter in the choosen word and replace it by the dashed lines
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"The Guess is correct!")

    print(display)

    # Losing of the game
    if guess not in chosen_word:
        print(f"You gussed the letter {guess}, that is not in the word, you lose a life.\nNow you have only {lives-1} lives left")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lose the game.\nThe word you failed to find is {chosen_word}")
     # Winning part
    if "_" not in display:
        game_over = True
        print("You won")

    print(stages[lives])