import random

# Initialisation
ranks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
face = ["K","Q","J"]
suits = ["S","H","C","D"]

# Reset Deck
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

    # Write deck to file
    file = open("deck.txt","w")
    for i in range(0,len(cardsUnshuffled)):
        file.write(cardsUnshuffled[i]+"\n")
    file.close()


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

    # Write deck to file
    file = open("deck.txt","w")
    for i in range(0,len(cardsUnshuffled)):
        file.write(cardsUnshuffled[i]+"\n")
    file.close()


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

    # Write deck to file
    file = open("deck.txt","w")
    for i in range(0,len(cardsUnshuffled)):
        file.write(cardsUnshuffled[i]+"\n")
    file.close()


def genErratic():
    cardsUnshuffled = []
    card = ""

    # Create 52 random cards
    for i in range(0,52):
        suit = suits[random.randint(0,3)]
        rank = ranks[random.randint(0,12)]
        card = rank + suit
        cardsUnshuffled.append(card)

    # Write deck to file
    file = open("deck.txt","w")
    for i in range(0,len(cardsUnshuffled)):
        file.write(cardsUnshuffled[i]+"\n")
    file.close()

def shuffleDeck():
    global deckSize
    # If file does not exist then create it
    cardsUnshuffled = []
    try:
        file = open("deck.txt", "r")
    except:
        genRegular()
        file = open("deck.txt", "r")
    card = file.readline().strip("\n")
    # Read deck from file
    while card != "":
        cardsUnshuffled.append(card)
        card = file.readline().strip("\n")
    deckSize = len(cardsUnshuffled)
    file.close()

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
    printShuffle(cardsShuffled)


def printShuffle(cardsShuffled):
    # Print shuffled card order
    for i in range(0,deckSize):
        cardName = ""
        # Rank
        match cardsShuffled[i][0]:
            case "A":
                cardName = cardName + "Ace of "
            case "K":
                cardName = cardName + "King of "
            case "Q":
                cardName = cardName + "Queen of "
            case "J":
                cardName = cardName + "Jack of "
            case "1":
                cardName = cardName + "Ten of "
            case "9":
                cardName = cardName + "Nine of "
            case "8":
                cardName = cardName + "Eight of "
            case "7":
                cardName = cardName + "Seven of "
            case "6":
                cardName = cardName + "Six of "
            case "5":
                cardName = cardName + "Five of "
            case "4":
                cardName = cardName + "Four of "
            case "3":
                cardName = cardName + "Three of "
            case "2":
                cardName = cardName + "Two of "
        # Suit
        match cardsShuffled[i][-1]:
            case "S":
                cardName = cardName + "Spades"
            case "H":
                cardName = cardName + "Hearts"
            case "C":
                cardName = cardName + "Clubs"
            case "D":
                cardName = cardName + "Diamonds"
        print(cardName)


def showMenu():
    print("\nMenu:\n1. Reset Deck\n2. Shuffle Deck\n3. Close")
    match int(input()):
        case 1:
            print("\nMenu:\n1. Regular\n2. Checkered\n3. Abandoned\n4. Erratic")
            choice = int(input())
            resetDeck(choice)
        case 2:
            print("\n")
            shuffleDeck()
        case 3:
            print("\n")
            global menu
            menu = False
        case _:
            print("\n")
            print("Invalid option.")


menu = True
while menu:
    showMenu()

# pyinstaller -F --icon=C:\pathtoyouricon\icon.ico --noconsole C:\pathtoyourscript\yourscript.py