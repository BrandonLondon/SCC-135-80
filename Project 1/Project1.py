# Author: Brandon London
# Date: 06/18/2020
# Version: 1
#===============================================================================
# Project Overview
# 
# In this project, you are given the grand prize (in dollars) and the winning numbers.  Your program will read multiple tickets (6 selected numbers in each ticket) from the user.  For each ticket, the program calculates its prize won, and outputs the prize (in dollars) to the user.
# 
# How to Play the Game?
# 
# In each game, the player selects 5 numbers from a set of 69 white balls (numbered 1 to 69) and one number from 26 red balls (numbered 1 to 26).  The red ball number can be the same as one of the white balls, but a white ball can only be selected once.  The order of selection does not matter.  The numbers in each ticket is not guaranteed to be sorted in any way.
#===============================================================================
#Initialize two empty arrays
winnigNumbers=[]
ticketNumbers=[]
#intialize winning numbers and grand prizes
GRAND_PRIZE = "$990,000,000"
WHITE = [14, 19, 39, 47, 51]
RED = 15
#set flag for repeat
flag = False
#put program into a while loop to repeat.
while flag == False:
    #double check loop is set to false
    flag = False
#Get users number and put it into a list
    userSelectedNumbers = input("Please put in 6 numbers seperated by spaces (first five are white last is red):")
    selectedNumbers = userSelectedNumbers.split(" ")
#assign the red number to varaible and remove it from the list
    redNumber = int(selectedNumbers[-1])
    whiteNumbers = selectedNumbers[:-1]
#Initalize variables to keep track of matches
    whiteMatches = 0
    redMatches = 0
     
    #Calculates number of white matches
    for userSelected in whiteNumbers:
        for x in WHITE:
            if int(x) == int(userSelected):
                
                whiteMatches = whiteMatches + 1
    
    #finds number of red matches  
    if int(redNumber) == int(RED):
        redMatches = 1
# this will compare how many matches there were and display the prize wont
    if (redMatches == 1 and whiteMatches == 0) or (redMatches == 1 and whiteMatches == 1):
        print("Your Prize: $4")
    elif (redMatches == 1 and whiteMatches == 2) or (whiteMatches == 3 and redMatches == 0):
        print("Your Prize: $7")
    elif (redMatches == 1 and whiteMatches == 3) or (whiteMatches == 4 and redMatches == 0):
        print("Your Prize: $100")
    elif redMatches == 1 and whiteMatches == 4:
        print("Your Prize: $50,000")
    elif whiteMatches == 5 and redMatches == 0:
        print("Your Prize: $50,000")
    elif redMatches == 1 and whiteMatches == 5:
        print("Your Prize: Grand Prize " + str(GRAND_PRIZE))
    else: 
        print("Your Prize: No Winnings, Try Again")
#ask if user would like to try again.
    restartProg = input("Would you like to try again? y/n")
#if they dont want to continue, thank them and change the flag to terminate the program
    if restartProg == "n" or restartProg == "no" or restartProg == "No":
        flag = True
        print("Thanks for playing")

