############################################################################################
### Black Jack 
############################################################################################
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 06 17:27:05 2018

@author: vmatcha
"""

from IPython.display import clear_output
import time 
import random

class Player(object):
    '''
    class for players of Blackjack
    attributes:
        Name: player input
        balance: $1000, the default amount available with player
    '''
    card_tot = 0	      # total value of cards where A is 1
    acard_tot = 0	      # total value of cards where A is 11
    bet_amount = 50     # amount bet by player 
    
    def __init__(self, player_no, player_name, balance=1000):
        self.player_no = player_no
        self.player_name = player_name
        self.balance = balance
    
    def add_balance(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw_balance(self, bet_amount):
        self.balance -= self.bet_amount
        return self.bet
    
    def add_won_amount(self, win_amount):
        self.balance += win_amount
        return win_amount
        
    def set_card_tot(self, card):
        if card in ['J','Q','K','A']:
            self.card_tot += 10
            if card == 'A':
                self.acard_tot += 11
        else:
            self.card_tot += int(card)      


#Dictionary to be used to display game board with values, Dealer is the Key '4'
dic={ 4:['Dealer', ['','','','','',''],['','']], 1:['player1', ['','','','','',''],['','']], 2:['player2', ['','','','','',''],['','']], 3:['player3', ['','','','','',''],['','']]}
deck = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']*4


def blackjack_board(dic):
    '''
    displays the updated Blackjack board, taking dictionary as input, where dictionary is of format:
    {1:['player1', ['c','a','r','d','s',''],['count','A-count']], 2: ..., 3: ..., 'd': ...}
    where dealer='d', players: 1,2,3
    '''
    clear_output()
    time.sleep(0.5) 
    
    print '|  \033[1m   Black Jack \033[0m'
    print '|--------------------------|-----------Dealer_--------|--------------------------|'
    print '|--------------------------| Cards:\033[1m {a1} {a2} {a3} {a4} {a5} {a6}     \033[0m -|--------------------------|'.format(a1=dic[4][1][0].ljust(1), a2=dic[4][1][1].ljust(1), a3=dic[4][1][2].ljust(1), a4=dic[4][1][3].ljust(1), a5=dic[4][1][4].ljust(1), a6=dic[4][1][5].ljust(1))
    print '|--------------------------| Count: {d1} / {d2}      -|--------------------------|'.format(d1=dic[4][2][0].ljust(4), d2=dic[4][2][1].ljust(4))
    print '|--------------------------|--------------------------|--------------------------|'
    print '|--------{d1}-----------|--------{d2}-----------|--------{d3}-----------|'.format(d1=dic[3][0].ljust(7), d2=dic[2][0].ljust(7), d3=dic[1][0].ljust(7))
    print '|-                        -|-                        -|-                        -|'
    print '| Cards:\033[1m {a1} {a2} {a3} {a4} {a5} {a6}     \033[0m -| Cards:\033[1m {b1} {b2} {b3} {b4} {b5} {b6}     \033[0m -| Cards:\033[1m {c1} {c2} {c3} {c4} {c5} {c6}     \033[0m -|'.format(a1=dic[3][1][0].ljust(1), a2=dic[3][1][1].ljust(1), a3=dic[3][1][2].ljust(1), a4=dic[3][1][3].ljust(1), a5=dic[3][1][4].ljust(1), a6=dic[3][1][5].ljust(1), b1=dic[2][1][0].ljust(1), b2=dic[2][1][1].ljust(1), b3=dic[2][1][2].ljust(1), b4=dic[2][1][3].ljust(1), b5=dic[2][1][4].ljust(1), b6=dic[2][1][5].ljust(1), c1=dic[1][1][0].ljust(1), c2=dic[1][1][1].ljust(1), c3=dic[1][1][2].ljust(1), c4=dic[1][1][3].ljust(1), c5=dic[1][1][4].ljust(1), c6=dic[1][1][5].ljust(1))
    print '| Count: {a1} / {a2}      -| Count: {b1} / {b2}      -| Count: {c1} / {c2}      -|'.format(a1=dic[3][2][0].ljust(4), a2=dic[3][2][1].ljust(4), b1=dic[2][2][0].ljust(4), b2=dic[2][2][1].ljust(4), c1=dic[1][2][0].ljust(4), c2=dic[1][2][1].ljust(4))
    print '|--------------------------|--------------------------|--------------------------|'
    print '| Bet: {a1}               -| Bet: {b1}               -| Bet: {c1}               -|'.format(a1=str(p1.bet_amount).ljust(4), b1=str(p2.bet_amount).ljust(4), c1=str(p3.bet_amount).ljust(4))
    print '| Balance: {a1}           -| Balance: {b1}           -| Balance: {c1}           -|'.format(a1=str(p1.balance).ljust(4), b1=str(p2.balance).ljust(4), c1=str(p3.balance).ljust(4))



def random_cards(cnt, deck):
    '''
    The function takes 2 arguments 'count of random cards' needed to be picked from 'Deck of cards'
    Returns the list 'rand_card' with the picked cards
    pops\removes the selected cards from the deck
    '''
    rand_card=[]
    while cnt>0:
        rand_card.append(deck.pop(deck.index(random.choice(deck))))
        cnt -= 1
    return rand_card



def hit_stand(deck, player_no, in_decision):
        '''
        Function takes arguments 'deck', 'player' and 'decision' to HIT(H) or STAND (S)
        updates the player dictionary with 6 cards allocated to him and the count of cards.
        If 'A' is part of cards delt, both counts with and without A are added to dictionary
        '''
        if in_decision == 'H':
            #print dic[player_no][1]
            card = str(random_cards(1, deck)) #convert to string so that the ljust() functoin can be appled in the board display
            dic[player_no][1].extend(card)
            dic[player_no][1]=dic[player_no][1][1:] #logic required to ensure the board display is not disturbed, by keeping 6 elements always
            print dic[player_no][1]
            
        else:
            pass

# Function to capture the player nmes based on the number of players in game
def getplayer_names(player_count):
    for i in xrange(1, player_count+1):
        name = raw_input('Enter the player %s name : ' %(i)).capitalize()
        dic[i][0] = name[:7]
	


# Begin Program for Blackjack :
print ("Welcome to Blackjack game!")

while True:
    try:
        player_count = input("Enter the number of players 1, 2 or 3: ")
    except:
        print 'Please enter valid number: 1 to 3'
    else:
        if player_count in (1,2,3):
            getplayer_names(player_count)
            break
        else:
            print 'Please enter number: 1 to 3'
            pass


# Create instances of Player()
dlr = Player(4, dic[4][0]) #Dealer is the Key '4'
p1 = Player(1, dic[1][0])
p2 = Player(2, dic[2][0])
p3 = Player(3, dic[3][0])


p_list = [dlr, p1, p2, p3]

blackjack_board(dic)


p1.bet_amount=input("{a} enter bet :".format(a=dic[1][0]))
p2.bet_amount=input("{a} enter bet :".format(a=dic[2][0]))
p3.bet_amount=input("{a} enter bet :".format(a=dic[3][0]))

blackjack_board(dic)

#Initially Deal 2 cards for each player and the Dealer
loop=2
while loop>0:
    for i in xrange(1, player_count+2):
        hit_stand(deck, i, 'H')
        blackjack_board(dic)
    else:
        pass
    loop -= 1
        


#Iterate through each player for Hit, Stand or Bust
for i in xrange(1, player_count+2):
    while True:
        play_hand = raw_input("Decide HIT or STAND :").upper()
        if play_hand[:1] not in ('H','S'):   #check just the first char.upper() entry by user
            print 'Valid decisions are only H,h or S,s:'
            continue
        else:
            #print play_hand
            #print deck
            hit_stand(deck, 1, play_hand)
            break #breaks from while loop
