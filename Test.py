import random

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suites = ['Hearts','Diamonds','Spades','Clubs']
Deck = [n + " of " + m for n in rank for m in suites]
print Deck

Count = 0
NewDeck = []
while Count < 26: 
    FirstHalf = Deck[:26]
    #print FirstHalf
    SecondHalf = Deck[-26:]
    #print SecondHalf
    
    NewDeck += [FirstHalf[Count]]
    NewDeck += [SecondHalf[Count]]
    Count += 1
print NewDeck

