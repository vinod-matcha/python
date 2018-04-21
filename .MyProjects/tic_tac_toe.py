# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 17:56:50 2018

@author: vmatcha
"""

def tic_tac_toe():
    '''
    Tic-Tac-Toe Game for 2 players
    '''
    import itertools
    repeat_game = 'Y'
    
    print "Welcome to TIC-TAC-TOE"
    
    while repeat_game == 'Y':
        # Confirm if user wants to play the game
        play_yn = raw_input("Continue to Play? Y :")
        if play_yn != 'Y':
            return 'Bye Bye...'  #"return" can be run only with in a function, if run seperately it will fail
        else:
            d_board = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}  #tic-tac-toe board display
            d_player = {'X':{'user':'', 'moves':[]}, 'O':{'user':'', 'moves':[]}}  #user details and moves made
            win_lst = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]  #Sorted tuples list with Winning combinations
            move_selected = []
            move_key = []
            p_cnt = 0
            game_over = 'N'
    
        print "\n2 players can play the game"
        print "The board will be printed out every time a player makes a move"
        while p_cnt < 2:
            if p_cnt == 0:
                #player.append(raw_input("Enter player 1 name :"))
                d_player['X']['user']=raw_input("Enter player 1 name :")
                p_cnt += 1
            elif p_cnt == 1:
               # player.append(raw_input("Enter player 2 name :"))
                d_player['O']['user']=raw_input("Enter player 2 name :")
                p_cnt += 1
       
        print "\nStarting game : {p1}: X    {p2}: O".format(p1 = d_player['X']['user'].upper(), p2 = d_player['O']['user'].upper())

        # switch active player: for every 'odd' k in d_boardtionary assign select player 1, for 'even' player 2
        # len(d_board)+2 to get 10 iterations instead of 9, where 9 is number of keys in d_boardtionary, to print final matrix summary
        for key in xrange(1, len(d_board) + 2):
            if key % 2 != 0:
                i='X'
            elif key % 2 == 0:
                i='O'
            else:
                pass
     
            # Printing the status of tic-tac-toe board
            print "       ", d_board[1], "|", d_board[2], "|", d_board[3]
            print "     ","----""----""-----"
            print "       ", d_board[4], "|", d_board[5], "|", d_board[6]
            print "     ","----""----""-----"        
            print "       ", d_board[7], "|", d_board[8], "|", d_board[9]
            
            # ensures d_board is printed only once after game is over
            if game_over == 'Y':
                break
            else:
                pass

            # need to reset check_move before every player move, so that move entered is validated
            check_move = 0 
            while check_move == 0 and key < 10 and game_over == 'N':
            #key = 1
            #while check_move == 0  and game_over == 'N':
                print "{p} make a move by selecting a square...".format(p=d_player[i]['user'].upper())
                move_selected = raw_input("Enter :")
                #ensure input made is numeric
                if move_selected not in ('1','2','3','4','5','6','7','8','9'):
                    print 'Enter valid number 1-9'
                    continue #will send control back to while loop
                else:
                    #ensure input made is acceptable move or not
                    move_key = int(move_selected)
                    if move_key not in d_player['O']['moves'] + d_player['X']['moves']:
                        d_player[i]['moves'].append(move_key)
                        
                        #Condition to check if player won the game
                        plyr_moves = list(itertools.combinations(d_player[i]['moves'], 3))
                        for combtns in plyr_moves:
                            cmb = list(combtns)  # Convert tuples to list, as data inside tuples cannnot be sorted
                            cmb.sort()
                            #print cmb
                            if cmb in win_lst:
                                print "\n {p1} - Won the Game !!! \n".format(p1 = d_player[i]['user'].upper())
                                game_over='Y' #ensures while loop for user input ends.
                            else:
                                if key == 9: # will enter this part only for the 9th iteration of for loop
                                    print "\n   - Game is a Draw - \n"
                                    game_over='Y'
                                    break
                        check_move += 1
                    else:
                        print "Move already used!"
                        continue
            d_board[move_key] = i
    