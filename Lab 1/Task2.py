# Author: Brandon London
# Date: 06/02/2020
# Version: 1
# Purpose: This program 
# 1) Read in five input values, which are the netBalance(float), payment(float), dOne (int), dTwo (int), and monthly rate of interest (float). Please note that the user of your program cannot see (or understand) your code, so you need to give sufficient screen prompts to tell the user what to input.
# 2) Calculate the interest based on the input values.
# 3) Show the calculated interest to the standard console (screen) in an understandable way to the use

flag = 'true'
#Set flag to true for loops
while flag == 'true':
#While flag is true perform operations below and repeat if necessary 

# variable definitions
    payment = float(input('Please indicate payment made (two decimal points)'))
    dOne = int(input('Please input the number of days into the billing cycle (Integers only)'))
    dTwo = int(input('Please input the number of payments made before billing cycle Integers Only)'))
    netBalance = float(input('Please input your net Balance'))
    rateOfInterest = float(input('Please input your monthly rate of interest'))
    interest = float()
    avgDailyBalance = float()
    
# Calculate the average daily Balance     
    avgDailyBalance = (((netBalance*dOne)-(payment*dTwo))/dOne)
# Print out the Average Daily Balance for Verifications
    print('Average Daily Balance: ', avgDailyBalance )
#Calculate the Interest
    interest = avgDailyBalance * rateOfInterest
# Pint out interest for user
    print('Interest: ', interest)
# Get user input so you can loop through the program
    redo = raw_input('Would you like to do the calculations again? y/n: ')
#Based on user response change the flag.
    if redo == 'y':
        
        flag = 'true'
    else:
        flag = 'null'
    
    