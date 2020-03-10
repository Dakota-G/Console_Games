import random

hangman_word_list = ["iterable", "python", "loops", "programs", "boolean", "variables", "conditionals", "lists", "expressions", "console", "technology"]

print("Let's play 'Guess The Word!")
print("Each turn, guess the letter you think is in the word! You win when the whole word is revealed! But don't run out of turns!")
# When we start a new game, we want to choose a random word from our word list and empty our guesses. If the students haven't learned random.choice yet, this is a good opportunity for that.
hangman_word = random.choice(hangman_word_list).lower()
guesses = []
gameover = False
turn_amount = 15
# We can use a for-loop as a game loop, and by setting a range, we can set the amount of loops (or turns) before the game ends
for turn in range(turn_amount):
# We set a boolean value as a check if the word has been solved and reset the display word so we can rebuild it, adding any correctly guessed letters to the console
    solved = True
    display = ""
# We go through the word and see if our guesses are correct. Correct guesses are displayed in-place, any letters we haven't guessed are displayed as a dash. Displaying a dash sets the solved boolean to False.
    for char in hangman_word:
        if char in guesses:
            display += char
        else:
            display += "-"
            solved = False
    print("Here is the word to guess: " +display)
# If the boolean 'solved' is False, that means the game isn't over. If it is True, then tell the player that they won
    if solved == False:
        correct = False
        turns_left = turn_amount - turn
        print(f"Turns left: {turns_left}")
        guess = input("What letter would you like to guess?").lower()
# This will check if we have already tried to guess the letter by checking the guessed letter bank
        for char in guesses:
            if char == guess:
                print("Sorry, you've guessed that letter!")
                break
# Let the player know whether they guessed correctly or not by pre-checking the guess against the word
        for char in hangman_word:
            if char == guess:
                correct = True
                print("Yes! That's a good guess!")
                break
    elif solved == True:
        print("YOU WIN!! The word was: " +hangman_word)
        break
    if correct == False:
        print("Sorry! That letter isn't correct!")
    guesses.append(guess)
# if the for-loop ends before the word is solved then the game ends
if solved == False:
    input("Sorry! You ran out of turns! Press Enter to close the game.")
    