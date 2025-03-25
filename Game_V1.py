import random
import time

cards = [
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
random.shuffle(cards)

# initialize decks
p1_Deck = []
cpu_Deck = []

board = []


# Welcome the user
print("Welcome to texas hold em python")
# promt the inital bet amount
inital_bet = int(input("How much do you want to bet? "))
preflopfin = False
# define dealing cards to the user 
def dealPreFlop():
    
    #set the amount of cards that have already been dealt to 0
    cardsDealt = 0
    #checks if theres less than 2 cards dealt
    while cardsDealt < 2:
        #gets a random card, adds it to players hand then removes it from deck
        card = random.randint(0, len(cards) -1)
        p1_Deck.append(cards[card])
        cards.pop(card)

        #repeats for the cpu's hand
        card2 = random.randint(0, len(cards) -1)
        cpu_Deck.append(cards[card2])
        cards.pop(card2)

        # add 1 card dealt
        cardsDealt +=1
    else:
        preflopfin = True
flopfin = False
# define showing the cards on the table
def dealFlop():
    
    #set the amount of cards that have already been dealt to 0
    flopcardsDealt = 0
    while preflopfin == True:
        #checks if theres less than 3 cards dealt
        while flopcardsDealt < 3:
            #gets a random card, adds it to table then removes it from deck
            randcard = random.randint(0, len(cards) -1)
            board.append(cards[randcard])
            cards.pop(randcard)

            # add 1 card dealt
            flopcardsDealt +=1
        else:
            flopfin = True

def betFlop():
    p1_ready = False
    while flopfin == True:
        action = input("what do you want to do (check, raise, fold)? ")

        if action.lower() == "check":
            p1_ready = True
        elif action.lower() == "raise":
            betamnt = int(input("How much do you want to bet? "))
            totalbetamnt = inital_bet + betamnt
            print(totalbetamnt)
        elif action.lower() == "fold":
            exit()

# start dealling initial cards to players
dealPreFlop()
#deal cards to the table
dealFlop()
betFlop()

print(f" Your Cards{p1_Deck}")
print(f" Opponents Cards{cpu_Deck}")
print(f"Table{board}")
print(f" cards left in deck{cards}")




# 25/3/25 start the dealing of cards to player 1
#26/03 deal cpu cards and table and adding flop bet