import collections, random

# TODO: 
# Needs a child class of dealer to hide the total value and first card in hand
# Add methods for the higher-level play? Split? Double Down? Etc

# Copying the card and Deck classes from FrenchDeck.py
card = collections.namedtuple('card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [card(rank, suit) for rank in self.ranks 
                                        for suit in self.suits]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

# Class for the player with will keep track of the cards in hand and the value of that hand, methods for play
class Player:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.hand = []
    def show_hand(self):
        for card in self.hand:
            print(f"{self.name} holds {card}")
    def calculate_value(self):
        self.value = 0
# Add together all the non-Ace cards
        for card in self.hand:
            if card.rank == "K" or card.rank == "Q" or card.rank == "J":
                self.value += 10
            elif card.rank == "A":
                continue
            else:
                self.value += int(card.rank)
# Make sure to check for Aces last
        for card in self.hand:
            if card.rank == 'A' and self.value < 11:
                self.value += 11
            elif card.rank == 'A' and self.value > 11:
                self.value += 1
        print(f"{self.name} has {self.value}")
    def hit(self, card):
        self.hand.append(card)
        self.calculate_value()
        self.show_hand()
    def stay(self):
        self.calculate_value()
        self.show_hand()
        print(f"{self.name} stays at {self.value}")

def first_deal(play_deck, my_deck, player, dealer):
    for card in my_deck:
        play_deck.append(card)
    x = 0
    while x < 2:
        dealer.hand.append(random.choice(play_deck))
        player.hand.append(random.choice(play_deck))
        x += 1
    player.show_hand()
    dealer.show_hand()
    player.calculate_value()
    dealer.calculate_value()

def ask_input(player, dealer, play_deck):
    stay = False
    while player.value < 21:
        hit = input("Would you like to hit? y or n?").lower()
        if hit == 'y' or hit == 'yes':
            player.hit(random.choice(play_deck))
        elif hit == 'n' or hit == 'no':
            stay = True
            break
        else:
            print("Please respond with a 'y' or 'n'.")
    if stay == True:
        return
    return print("Player busted!")
            
def dealer_play(dealer, player, play_deck):
    while dealer.value <= player.value:
        dealer.hit(random.choice(play_deck))

def check_win(player, dealer):
    if dealer.value > 21 or player.value > dealer.value:
        return print("Player wins!")
    else:
        return print("Player loses!")

def start_game():
    player = Player(input("what is your name?"))
    dealer = Player("Dealer")
    my_deck = Deck()
    play_deck = []
    first_deal(play_deck, my_deck, player, dealer)
    ask_input(player, dealer, play_deck)
    dealer_play(dealer, player, play_deck)
    check_win(player, dealer)

start_game()