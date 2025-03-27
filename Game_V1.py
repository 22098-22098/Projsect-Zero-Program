import random
import time

deck = [
    "K♣️","K♠️","K♥️","K♦️",
    "Q♣️","Q♠️","Q♥️","Q♦️",
    "J♣️","J♠️","J♥️","J♦️",
    "10♣️","10♠️","10♥️","10♦️",
    "9♣️","9♠️","9♥️","9♦️",
    "8♣️","8♠️","8♥️","8♦️",
    "7♣️","7♠️","7♥️","7♦️",
    "6♣️","6♠️","6♥️","6♦️",
    "5♣️","5♠️","5♥️","5♦️",
    "4♣️","4♠️","4♥️","4♦️",
    "3♣️","3♠️","3♥️","3♦️",
    "2♣️","2♠️","2♥️","2♦️",
    "A♣️","A♠️","A♥️","A♦️",
]

# shuffle deck
random.shuffle(deck)

# initialize decks
p1_Hand = []
cpu_Hand = []

board = []

# Welcome the user
print()
print("Welcome To Texas Hold-Em Python")
print()
# promt the inital bet amount
inital_bet = int(input("How much do you want to bet?\n"))

'''
#=============== Add dealing deck to the user ====================#
'''
#set the amount of deck that have already been dealt to 0
deckDealt = 0
#checks if theres less than 2 deck dealt
while deckDealt < 2:
    #gets a random card, adds it to players hand then removes it from deck
    card = random.randint(0, len(deck) -1)
    p1_Hand.append(deck[card])
    deck.pop(card)

    #repeats for the cpu's hand
    card2 = random.randint(0, len(deck) -1)
    cpu_Hand.append(deck[card2])
    deck.pop(card2)

    # add 1 card dealt
    deckDealt +=1


print()
print(f"Your deck{p1_Hand}")
print()


'''
#===================== Add the deck on the table ===================#
'''

#set the amount of deck that have already been dealt to 0
flopdeckDealt = 0
#checks if theres less than 3 deck dealt
while flopdeckDealt < 3:
    #gets a random card, adds it to table then removes it from deck
    randcard = random.randint(0, len(deck) -1)
    board.append(deck[randcard])
    deck.pop(randcard)

    # add 1 card dealt
    flopdeckDealt +=1

print(f"Table{board}")

'''
#==================== second betting round =========================#
'''

action = input("what do you want to do (check, raise, fold)?\n")

if action.lower() == "check":
    print("READY")
elif action.lower() == "raise":
    betamnt = int(input("How much do you want to bet? "))
    totalbetamnt = inital_bet + betamnt
    print(totalbetamnt)
elif action.lower() == "fold":
    exit()






#25/3/25 start the dealing of deck to player 1
#26/03 deal cpu deck and table and adding flop bet
#27/03 fix functions not waiting for eachother and titled sections of the code to make it easier to read