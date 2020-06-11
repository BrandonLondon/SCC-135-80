# Author: Brandon London
# Date: 06/11/2020
# Version: 1
# Purpose:This Program opens a file, splits the lines up, adds the first 2 number pair together
# then organizes those numbers from gold, silver and bronze

#Open Up the file
f = open("input.txt","r")
# create and open the output file with write capabilities
outputFile = open("output.txt", "w+")
# from the input put the data into a list seperated by new lines
playerScores = f.read().split("\n")
# for every pair of numbers add then together to get the total score
playerOneScore = (float(playerScores[0]) + float(playerScores[1]))
playerTwoScore = (float(playerScores[2]) + float(playerScores[3]))
playerThreeScore = (float(playerScores[4]) + float(playerScores[5]))
#Gold value will always be the max of these three variables (it finds the greatest number)
gold = max(playerOneScore, playerTwoScore, playerThreeScore)
#bronze value will always be the min of these three variables (it finds the smallest number)
bronze = min(playerOneScore, playerTwoScore, playerThreeScore)
# we want to go ahead and output the gold to the file and make sure its formated to two decimal place
outputFile.write('Gold: {:0.2f}\n'.format(gold))
# We now need to find silver, We have already found bronze and Gold so lets just check to see if its between those
#These if statements are for the three players as we will ever only have 3 players
if playerOneScore < gold and playerOneScore > bronze:
    outputFile.write('Silver: {:0.2f}\n'.format(playerOneScore))
elif playerTwoScore < gold and playerTwoScore > bronze:
    outputFile.write('Silver: {:0.2f}\n'.format(playerTwoScore))
elif playerThreeScore < gold and playerThreeScore > bronze:
    outputFile.write('Silver: {:0.2f}\n'.format(playerThreeScore)) 
  
# We already know the bronze as we found the min score above so we just need to print it in the correct format
outputFile.write('Bronze: {:0.2f}\n'.format(bronze))
# we always want to make sure we close the file
outputFile.close()
f.close()