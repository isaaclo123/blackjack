# -*- coding: utf-8 -*-

from random import randint

def shuffle():
    global cards
    cards = {"A♠":1, "2♠":2, "3♠":3, "4♠":4, "5♠":5, "6♠":6, "7♠":7, "8♠":8, "9♠":9, "10♠":10, "J♠":10, "Q♠":10, "K♠":10, "A♥":1, "2♥":2, "3♥":3, "4♥":4, "5♥":5, "6♥":6, "7♥":7, "8♥":8, "9♥":9, "10♥":10, "J♥":10, "Q♥":10, "K♥":10, "A♦":1, "2♦":2, "3♦":3, "4♦":4, "5♦":5, "6♦":6, "7♦":7, "8♦":8, "9♦":9, "10♦":10, "J♦":10, "Q♦":10, "K♦":10, "A♣":1, "2♣":2, "3♣":3, "4♣":4, "5♣":5, "6♣":6, "7♣":7, "8♣":8, "9♣":9, "10♣":10, "J♣":10, "Q♣":10, "K♣":10}

def deal(player, dealnum):
    global cards
    if len(cards) <= 0 :
        shuffle()
    if player[2] == True :
        for x in xrange (0,dealnum) :
            therandomint = randint(0,len(cards) - 1)
            player[0] = player[0] + cards.keys()[therandomint] + " "
            player[1] = player[1] + cards[cards.keys()[therandomint]]
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
    global noshow
    character = ["", 0, True]
    character = deal(character,2)
    dealer = ["", 0, True]
    dealer = deal(dealer,2)
    noshow = True

def thedealer():
    if character[2] == True :
            while (dealer[1] < character[1]) & (dealer[2] == True):
                deal(dealer,1)

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
    printout(noshow)
    theinput = raw_input('command: ')
    print "\n" * 100
    if str(theinput) == "h" :
        deal(character,1)
    elif str(theinput) == "s" :
        thedealer()
        noshow = False
    elif str(theinput) == "r" :
        reset()
    elif str(theinput) == "q" :
        exit()