import random

# Initialisation
ranks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
face = ["K","Q","J"]
suits = ["S","H","C","D"]

# Generate Deck Functions
def resetDeck(choice):
    match choice:
        case 1:
            genRegular()
        case 2:
            genCheckered()
        case 3:
            genAbandoned()
        case 4:
            genErratic()
        case _:
            print("Invalid choice.")

def genRegular():
    cardsUnshuffled = []
    card = ""
    # Create every suit & rank
    for i in suits:
        for j in ranks:
            # Create card + add to list
            card = j + i
            cardsUnshuffled.append(card)

    writeDeck(cardsUnshuffled)

def genCheckered():
    cardsUnshuffled = []
    card = ""
    # Create every suit
    for i in suits:
        # Create every rank
        for j in ranks:
            # Create card + add to list
            rank = j
            suit = i
            # Only two suits
            if suit == "D":
                suit = "H"
            elif suit == "C":
                suit = "S"
            card = rank + suit
            cardsUnshuffled.append(card)

    writeDeck(cardsUnshuffled)

def genAbandoned():
    cardsUnshuffled = []
    card = ""
    # Create every suit
    for i in suits:
        # Create every rank
        for j in ranks:
            # Create card + add to list
            rank = j
            suit = i
            # Only add non face cards to deck
            if not rank in face:
                card = rank + suit
                cardsUnshuffled.append(card)

    writeDeck(cardsUnshuffled)

def genErratic():
    cardsUnshuffled = []
    card = ""

    # Create 52 random cards
    for i in range(0,52):
        suit = suits[random.randint(0,3)]
        rank = ranks[random.randint(0,12)]
        card = rank + suit
        cardsUnshuffled.append(card)

    writeDeck(cardsUnshuffled)

# File Functions
def writeDeck(cards):
    # Write deck to file
    file = open("deck.txt","w")
    for i in range(0,len(cards)):
        file.write(cards[i]+"\n")
    file.close()

def readDeck():
    cards = []
    try:
        file = open("deck.txt", "r")
    except:
        genRegular()
        file = open("deck.txt", "r")
    
    card = file.readline().strip("\n")
    # Read deck from file
    while card != "":
        cards.append(card)
        card = file.readline().strip("\n")
    file.close()
    return cards

def printDeck(cards):
    rankNames = ["Ace of ","King of ","Queen of ","Jack of ","Ten of ","Nine of ","Eight of ","Seven of ","Six of ","Five of ","Four of ","Three of ","Two of "]
    suitNames = ["Spades","Hearts","Clubs","Diamonds"]
    # String
    for card in cards:
        cardName = ""
        for rank in ranks:
            if str(card).startswith(rank):
                cardName = cardName + rankNames[ranks.index(rank)]
        for suit in suits:
            if str(card).endswith(suit):
                cardName = cardName + suitNames[suits.index(suit)]
        print(cardName)

# Sorting/Shuffle Functions
def parse_card(card):
    for rank in ranks:
        if str(card).startswith(rank):
            suit = card[len(rank):]
            return rank, suit
    return None, None  # fallback

def sortDeck(choice):
    match choice:
        case 1:
            sortDeckRank()
        case 2:
            sortDeckSuit()
        case _:
            print("Invalid choice.")

def sortDeckSuit():
    global deckSize
    # If file does not exist then create it
    cardsUnsorted = readDeck()

    def card_key(card):
        rank, suit = parse_card(card)
        return (suits.index(suit), ranks.index(rank))
    cardsSorted = sorted(cardsUnsorted, key=card_key)
    writeDeck(cardsSorted)

def sortDeckRank():
    global deckSize
    # If file does not exist then create it
    cardsUnsorted = readDeck()

    def card_key(card):
        rank, suit = parse_card(card)
        return (ranks.index(rank), suits.index(suit))
    cardsSorted = sorted(cardsUnsorted, key=card_key)
    writeDeck(cardsSorted)

def shuffleDeck():
    global deckSize
    # If file does not exist then create it
    cardsUnshuffled = readDeck()

    # Shuffle cards
    cardsShuffled = []
    cardsIndexed = []
    deckSize = len(cardsUnshuffled)
    while len(cardsShuffled) != deckSize:
        # Validate the card
        cardValid = False
        while not cardValid:
            cardValid = True
            # Generate random card
            shuffle = random.randint(0,deckSize-1)
            for i in range(0,len(cardsIndexed)):
                if shuffle == cardsIndexed[i]:
                    cardValid = False
        # Place into deck
        cardsIndexed.append(shuffle)
        cardsShuffled.append(cardsUnshuffled[shuffle])
    writeDeck(cardsShuffled)

# Menu
def showMenu():
    print("\nMenu:\n1. Reset Deck\n2. Shuffle Deck\n3. Sort Deck\n4. Print Deck\n5. Close")
    match int(input()):
        case 1:
            print("\nDeck:\n1. Regular\n2. Checkered\n3. Abandoned\n4. Erratic")
            choice = int(input())
            resetDeck(choice)
        case 2:
            print("\n")
            shuffleDeck()
        case 3:
            print("\n")
            print("\nSort:\n1. Rank\n2. Suit")
            choice = int(input())
            sortDeck(choice)
        case 4:
            print("\n")
            printDeck(readDeck())
        case 5:
            global menu
            menu = False
        case _:
            print("\n")
            print("Invalid option.")


menu = True
while menu:
    showMenu()

# pyinstaller -F --icon=C:\pathtoyouricon\icon.ico --noconsole C:\pathtoyourscript\yourscript.py