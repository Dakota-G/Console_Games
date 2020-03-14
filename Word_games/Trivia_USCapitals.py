import random

capitals = {
    "Alabama" : "Montgomery",
    "Alaska" : "Juneau",
    "Arizona" : "Phoenix",
    "Arkansas" : "Little Rock",
    "California" : "Sacramento",
    "Colorado" : "Denver",
    "Connecticut" : "Hartford",
    "Delaware" : "Dover",
    "Florida" : "Tallahassee",
    "Georgia" : "Atlanta",
    "Hawaii" : "Honolulu",
    "Idaho" : "Boise",
    "Illinois" : "Springfield",
    "Indiana" : "Indianapolis",
    "Iowa" : "Des Moines",
    "Kansas" : "Topeka",
    "Kentucky" : "Frankfort",
    "Lousiana" : "Baton Rouge",
    "Maine" : "Augusta",
    "Maryland" : "Annapolis",
    "Michigan" : "Lansing",
    "Minnesota" : "Saint Paul",
    "Mississippi" : "Jackson",
    "Missouri" : "Jefferson City",
    "Montana" : "Helena",
    "Nebraska" : "Lincoln",
    "Nevada" : "Carson City",
    "New Hampshire" : "Concord",
    "New Jersey" : "Trenton",
    "New Mexico" : "Santa Fe",
    "New York" : "Albany",
    "North Carolina" : "Raleigh",
    "North Dakota" : "Bismarck", 
    "Ohio" : "Columbus",
    "Oklahoma" : "Oklahoma City",
    "Oregon" : "Salem",
    "Pennsylvania" : "Harrisburg",
    "Rhode Island" : "Providence",
    "South Carolina" : "Columbia",
    "South Dakota" : "Pierre",
    "Tennessee" : "Nashville",
    "Texas" : "Austin",
    "Utah" : "Salt Lake City", 
    "Vermont" : "Montpelier",
    "Virginia" : "Richmond",
    "Washington" : "Olympia",
    "West Virginia" : "Charleston",
    "Wisconsin" : "Madison",
    "Wyoming" : "Cheyenne"
} 

def Start_Game():
    score = 0
    global capitals
    capitals_list = [state for state in capitals]
    rounds = select_rounds()
    while len(capitals_list) >= (50 - rounds):
        rando = random.randint(0, len(capitals_list))
        guess = input(f"What is the capital of {capitals_list[rando]}").lower()
        if guess != capitals[capitals_list[rando]].lower():
            print("Sorry, that is wrong!")
            guess2 = input(f"Try Again! What is the capital of {capitals_list[rando]}").lower()
            if guess2 != capitals[capitals_list[rando]].lower():
                print("Sorry, that is wrong too!")
            else:
                print("Correct!")
                score += 1
        else:
            print("Correct!")
            score += 2
        capitals_list.pop(rando)
        print(f"Your score is {score}")
    print(f"Game over! You ended with a score of {score}!")
    input("Press any key to get quizzed again!")
    Start_Game()

def select_rounds():
    rounds = input("How many states would you like to try?")
    try: 
        rounds = int(rounds)
    except:
        print("Please use an integer between 1 and 50!")
        select_rounds()
    if rounds < 1 or rounds > 50:
        print("Please use an integer between 1 and 50!")
        select_rounds()
    return rounds

Start_Game()