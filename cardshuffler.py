import random

# Create deck of cards
deckSize = 52
cardsUnshuffled = []
ranks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2",]
suits = ["S","H","C","D",]

card = ""

# Create every suit
for i in suits:
    # Create every rank
    for j in ranks:
        # Create card + add to list
        card = j + i
        cardsUnshuffled.append(card)

# Shuffle cards
cardsShuffled = []
cardsIndexed = []
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

input("\nPress Enter to Exit")