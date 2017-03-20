import sys
sys.path.append('../Module')
import WulfModule

import random
import time


#choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'stafish', 'woodchuck', 'crab']

# This will initialize the cards into a random order

def InitilizeAndShuffle(choices):
    #choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'stafish', 'woodchuck', 'crab']
    #cards = ["", "", "", "", "", "", "", "", ""]
    matchCard = random.randrange(0,10)
    choices.append(choices[matchCard])
    random.shuffle(choices)
    #cards[0] = choices[0]
    #cards[1] = choices[1]
    #cards[2] = choices[2]
    #cards[3] = choices[3]
    #cards[4] = choices[4]
    #cards[5] = choices[5]
    #cards[6] = choices[6]
    #cards[7] = choices[7]
    #cards[8] = choices[8]
    return choices
    
def PickTwoCards(choices):
    keepGoing = True
    goodCard1 = True
    goodCard2 = True
    match = False
    Attempts = 0
    
    while keepGoing == True:
        print "Pick a card between 0 and 9"
        while goodCard1 == True:
            cardOne = WulfModule.UserInt("Pick card number one:")
            if(cardOne < 0 or cardOne > 9):
                print "Choose a card between 1 and 9"
            else:
                break
                
        while goodCard2 == True:
            cardTwo = WulfModule.UserInt("Pick card number two:")
            if(cardTwo < 0 or cardTwo > 9):
                print "Choose a card between 0 and 9"
            else: 
                break
    
        print "Card %s is a %s" %(cardOne, choices[cardOne])
        print "Card %s is a %s" %(cardTwo, choices[cardTwo])
        Attempts += 1
        
        
    
        if(choices[cardOne] == choices[cardTwo]):
            print "You won!"
            keepGoing = False
            print "It took you %s attempts to win" %(Attempts)
    

def Main():
    choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'stafish', 'woodchuck', 'crab']
    InitilizeAndShuffle(choices)
    PickTwoCards(choices)
    
    

Main()