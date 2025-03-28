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
    inital_bet += betamnt
    print(inital_bet)
elif action.lower() == "fold":
    exit()

check = p1_Hand + board
hearts = 0
diamonds = 0
spades = 0
clubs = 0
win = 0
for i in check:
    if "♥️" in i:
        hearts += 1
    if "♦️" in i:
        diamonds += 1
    if "♠️" in i:
        spades += 1
    if "♣️" in i:
        clubs += 1

cpu_check = cpu_Hand + board
cpu_hearts = 0
cpu_diamonds = 0
cpu_spades = 0
cpu_clubs = 0
cpu_win =0

for i in cpu_check:
    if "♥️" in i:
        cpu_hearts += 1
    if "♦️" in i:
        cpu_diamonds += 1
    if "♠️" in i:
        cpu_spades += 1
    if "♣️" in i:
        cpu_clubs += 1

if cpu_hearts == 3 or cpu_diamonds == 3 or cpu_spades == 3 or cpu_clubs == 3:
    cpu_win = 3
elif cpu_hearts == 2 or cpu_diamonds == 2 or cpu_spades == 2 or cpu_clubs == 2:  
    cpu_win = 2
elif cpu_hearts == 1 or cpu_diamonds == 1 or cpu_spades == 1 or cpu_clubs == 1:
    cpu_win = 1

if hearts == 3 or diamonds == 3 or spades == 3 or clubs == 3:
    win = 3
elif hearts == 2 or diamonds == 2 or spades == 2 or clubs == 2:  
    win = 2
elif hearts == 1 or diamonds == 1 or spades == 1 or clubs == 1:
    win =1



print(f"opponent had {cpu_Hand} so")
if win > cpu_win:
    print(win)
    print(cpu_win)
    print(f"you won ${inital_bet * 2}")
elif win == cpu_win:
    print(f"you draw you get ${inital_bet} back")
else:
    print(win)
    print(cpu_win)
    print(f"You lost ${inital_bet}")


#25/3/25 start the dealing of deck to player 1
#26/03 deal cpu deck and table and adding flop bet
#27/03 fix functions not waiting for eachother and titled sections of the code to make it easier to read
#28/03 added check to see who wins