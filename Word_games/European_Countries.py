import time

# TODO:
# Utilize a timer
# Return list of missed countries at the end

def start_game():
    countries = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium",
            "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
            "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", 
            "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Lativa",
            "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco",
            "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
            "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
            "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", 
            "Vatican City (Holy See)"]
    guesses = []
    input("Press any key when ready. Name as many European countries as you can. Spelling counts!")
    while len(countries) > 0:
        guess = input("Enter a European country:")
        if guess not in countries:
            if guess not in guesses:
                print("Incorrect! Try Again!")
            else:
                print("You already got that one!")
        else:
            print("Correct!")
            guesses.append(countries.pop(countries.index(guess)))
    print("You got all the European countries! Good job!")
    input("Press any key to start again!")
    start_game()

start_game()