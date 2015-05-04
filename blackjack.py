# -*- coding: utf-8 -*-

from random import randint

cards = {"A♠":1, "2♠":2, "3♠":3, "4♠":4, "5♠":5, "6♠":6, "7♠":7, "8♠":8, "9♠":9, "10♠":10, "J♠":10, "Q♠":10, "K♠":10, "A♥":1, "2♥":2, "3♥":3, "4♥":4, "5♥":5, "6♥":6, "7♥":7, "8♥":8, "9♥":9, "10♥":10, "J♥":10, "Q♥":10, "K♥":10, "A♦":1, "2♦":2, "3♦":3, "4♦":4, "5♦":5, "6♦":6, "7♦":7, "8♦":8, "9♦":9, "10♦":10, "J♦":10, "Q♦":10, "K♦":10, "A♣":1, "2♣":2, "3♣":3, "4♣":4, "5♣":5, "6♣":6, "7♣":7, "8♣":8, "9♣":9, "10♣":10, "J♣":10, "Q♣":10, "K♣":10}

def shuffle():
    global cards
    cards = {"A♠":1, "2♠":2, "3♠":3, "4♠":4, "5♠":5, "6♠":6, "7♠":7, "8♠":8, "9♠":9, "10♠":10, "J♠":10, "Q♠":10, "K♠":10, "A♥":1, "2♥":2, "3♥":3, "4♥":4, "5♥":5, "6♥":6, "7♥":7, "8♥":8, "9♥":9, "10♥":10, "J♥":10, "Q♥":10, "K♥":10, "A♦":1, "2♦":2, "3♦":3, "4♦":4, "5♦":5, "6♦":6, "7♦":7, "8♦":8, "9♦":9, "10♦":10, "J♦":10, "Q♦":10, "K♦":10, "A♣":1, "2♣":2, "3♣":3, "4♣":4, "5♣":5, "6♣":6, "7♣":7, "8♣":8, "9♣":9, "10♣":10, "J♣":10, "Q♣":10, "K♣":10}

def deal(player, dealnum):
    global cards
    if len(cards) <= 0 :
        shuffle()
        
    for x in xrange (0,dealnum) :
        therandomint = randint(0,len(cards) - 1)
        player[0] = player[0] + cards.keys()[therandomint] + " "
        player[1] = player[1] + cards[cards.keys()[therandomint]]
        cards.pop(cards.keys()[therandomint])
    return player

def reset():
    global character
    global dealer
    character = ["", 0]
    character = deal(character,2)
    dealer = ["", 0]
    dealer = deal(dealer,2)
    
def printout(hide):
    global character
    global dealer
    print "player: " + str(character[0])
    print "cardvalue: " + str(character[1]) + "\n"  
    if hide == True :
        print "dealer: " + "██" + dealer[0][4:]
    elif hide == False:
        print "dealer: " + str(dealer[0])
    if hide == True:
        print "dealercardvalue: ██"
    elif hide == False :        
        print "dealercardvalue: " + str(dealer[1]) + "\n"
    print "counter: " + str(len(cards)) + "\n"

print "BLACKJACK\nCopyright Isaac Lo 2015\n"
shuffle()
reset()

while True :
    theinput = raw_input('command: ')
    print "\n" * 100
    if str(theinput) == "s" :
        shuffle()
        reset()
        printout(True)
    elif str(theinput) == "d" :
        character = deal(character,1)
        printout(True)
    elif str(theinput) == "r" :
        reset()
        printout()
    elif str(theinput) == "q" :
        break
        exit()
        
    