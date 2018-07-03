# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:48:26 2018

@author: Ragini
"""

#%%

#Qn 2, Week 2 Homework Q1

#Make a list of all the possible spots a player may enter his symbol into
choices = []

#Make a number of these choices from 1-9 

for i in range(0,9):
    choices.append(str(i+1))

#Set a boolean, to initialise the game & to indicate there is no winner yet

player_one_turn = True
winner = False>

#Function to print out the tic tac toe board
def gameboard():
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')
    
#make a continuous loop so the game continues before a winner is decided
#not False == True
while not winner:
    
    gameboard()
    
    if player_one_turn:
        print("Player 1: ")
    else:
        print("Player 2: ")
        
    try:
        #Find the number square in which they want to add their symbol
        sq = int(input(">>"))
    except:
        print("Please enter a valid square number")
        continue
    
    #If this sq already occupies a X or a O
    if choices[sq-1] == 'X' or choices[sq-1] == 'O':
        print("This square is taken")
        continue
    
    #Inserting a symbol in the specific square
    if player_one_turn:
        #Auto assign the symbol the player should use
        choices[sq-1] = 'X'
    else:
        choices[sq-1] = 'O'
        
    player_one_turn =  not player_one_turn
    
    #x here, refer to the list indexs. so this range zooms into 0,1,2 
    for vertical in range(0,3):
        hori = vertical*3
        
        #What are the values of y that can come here? 0,1,2 (top row) 3,4,5(middle row) 6,7,8(bottom row)
        if(choices[hori] == choices[hori+1] and choices[hori] == choices[hori+2]):
            winner = True
            gameboard()
            
        #What are the values of x that can come here? 0,3,6(left vert) 1,4,7(centre vertical) 2,5,8 (right vert)
        elif(choices[vertical] == choices[vertical+3] and choices[vertical] == choices[vertical+6]):
            winner = True
            gameboard()
            
            
    #These are checkers for the diagonal wins, (left diag and right diag)        
    if((choices[0] == choices[4] == choices[8]) or (choices[2] == choices[4] == choices[6])):
        winner = True
        gameboard()
       
print("Player " +str(int(player_one_turn+1)) + " won!")
        
    














