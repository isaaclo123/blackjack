# -*- coding: utf-8 -*-

from random import randint
from numpy import character

def shuffle():
    global cards
    cards = {"A♠":0, "2♠":2, "3♠":3, "4♠":4, "5♠":5, "6♠":6, "7♠":7, "8♠":8, "9♠":9, "10♠":10, "J♠":10, "Q♠":10, "K♠":10, "A♥":0, "2♥":2, "3♥":3, "4♥":4, "5♥":5, "6♥":6, "7♥":7, "8♥":8, "9♥":9, "10♥":10, "J♥":10, "Q♥":10, "K♥":10, "A♦":0, "2♦":2, "3♦":3, "4♦":4, "5♦":5, "6♦":6, "7♦":7, "8♦":8, "9♦":9, "10♦":10, "J♦":10, "Q♦":10, "K♦":10, "A♣":0, "2♣":2, "3♣":3, "4♣":4, "5♣":5, "6♣":6, "7♣":7, "8♣":8, "9♣":9, "10♣":10, "J♣":10, "Q♣":10, "K♣":10}

def deal(player, dealnum):
    global cards
    if len(cards) <= 1 :
        shuffle()
    if player[2] == True:
        for x in xrange (0,dealnum) :
            therandomint = randint(0,len(cards) - 1)
            player[0] = player[0] + cards.keys()[therandomint] + " "
            player[1] = player[1] + cards[cards.keys()[therandomint]]
            if cards[cards.keys()[therandomint]] == 0 or player[1] > 21:
                if player[1] + 11 <= 21 :
                    player[1] = player[1] + 11
                    player[3] = player[3] + 1
                elif player[1] + 11 > 21 :
                    if player[1] + 1 <= 21 :
                        player[1] = player[1] + 1
                    elif player[1] + 1 > 21 and player[3] > 0 :
                        player[1] = player[1] - 10
                        player[3] = player[3] - 1
            cards.pop(cards.keys()[therandomint])
            if player[1] > 21 :
                player[0] = player[0] + "bust"
                player[2] = False
    return player

def dealer():
    global dealer
    global character
    
            
def reset():
    global character
    global dealer
    character = ["", 0, True, 0]
    character = deal(character,2)
    dealer = ["", 0, True, 0]
    dealer = deal(dealer,2)

def thedealer():
    if character[2] == True :
            while (dealer[1] < character[1]) and (dealer[2] == True):
                deal(dealer,1)
                
def checkwin():
    global character
    global dealer
    if ((character[1] > dealer[1]) and character[2] == True) or (character[2] == True and dealer[2] == False) :
        print "You have won!\n"
    elif ((character[1] < dealer[1]) and dealer[2] == True) or (character[2] == False and dealer[2] == True):
        print "The dealer has won!\n"
    elif dealer[1] == character[1] or (dealer[2] == False and character[2] == False) :
        print "Tie\n"
        
def stay():
    thedealer()
    printout(False)
    checkwin()
    raw_input("Press Enter to continue...")
    reset()

def printout(hide):
    global character
    global dealer
    print "\n" * 100
    print "player: " + str(character[0])
    print "cardvalue: " + str(character[1]) + "\n"  
    if hide == True :
        print "dealer: " + "██" + dealer[0][4:]
        print "dealercardvalue: ██"
    elif hide == False:
        print "dealer: " + str(dealer[0])
        print "dealercardvalue: " + str(dealer[1]) + "\n"
    print "counter: " + str(len(cards)) + "\n"

print "BLACKJACK\n\nCopyright Isaac Lo 2015\n"
raw_input("Press Enter to continue...")
print "\n" * 100
shuffle()
reset()
while True :
    #while True :
    printout(True)
    theinput = raw_input('command: ')
    print "\n" * 100
    if str(theinput) == "h" :
        deal(character,1)
    elif str(theinput) == "s" :
        stay()
    elif str(theinput) == "r" :
        reset()
    elif str(theinput) == "q" :
        exit()