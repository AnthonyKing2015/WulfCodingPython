import sys
sys.path.append('../Module')
import WulfModule
import random

#rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
#suites = ['Hearts','Diamonds','Spades','Clubs']

def BuildDeck(rank, suites):
    Deck = [n + " of " + m for n in rank for m in suites]
    return Deck


def Shuffle(Deck):
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
    return NewDeck
        
            
    


def Deal(deck):
    print deck[:5]
    


def Main():
    rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    suites = ['Hearts','Diamonds','Spades','Clubs']
    d = BuildDeck(rank, suites) 
    UserInput = WulfModule.UserInt("How many times would you like to shuffle?")
    for i in range(0, UserInput):
        d = Shuffle(d)
    Deal(d)
    
    
    
Main()