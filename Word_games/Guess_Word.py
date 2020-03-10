import random

hangman_word_list = ["iterable", "python", "loops", "programs", "boolean", "variables", "conditionals", "lists", "expressions", "console", "technology"]

def start_game():
    print("Let's play 'Guess The Word!")
    print("Each turn, guess the letter you think is in the word! You win when the whole word is revealed!")
# When we start a new game, we want to choose a random word from our word list and empty our guesses. If the students haven't learned random.choice yet, this is a good opportunity for that.
    hangman_word = random.choice(hangman_word_list).lower()
    guesses = []
    return render_word(hangman_word, guesses)

def render_word(hangman_word, guesses):
# We set a boolean value to let us know if the word has been solved and reset the display word so we can rebuild it, adding any correctly guessed letters to the console
    solved = True
    display = ""
# We go through the word and see if our guesses are correct. Correct guesses are displayed in-place, any letters we haven't guessed are displayed as a dash.
    for char in hangman_word:
        if char in guesses:
            display += char
        else:
            display += "-"
            solved = False
    print("Here is the word to guess: " +display)
# If the boolean 'solved' is False, that means the game isn't over. If it is True, then tell the player that they won
    if solved == False:
        return make_guess(hangman_word, guesses)
    input("You Win! Press Enter to Play Again!")
    return start_game()

def make_guess(hangman_word, guesses):
    correct = False
    guess = input("What letter would you like to guess?").lower()
# This will check if we have already tried to guess the letter
    for char in guesses:
        if char == guess:
            print("Sorry, you've guessed that letter!")
            return make_guess(hangman_word, guesses)
# Let the player know whether they guessed correctly or not
    for char in hangman_word:
        if char == guess:
            correct = True
            print("Yes! That's a good guess!")
    if correct == False:
        print("Sorry! That letter isn't correct!")
    guesses.append(guess)
    return render_word(hangman_word, guesses)

start_game()