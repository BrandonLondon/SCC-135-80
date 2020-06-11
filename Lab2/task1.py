# Author: Brandon London
# Date: 06/11/2020
# Version: 1
# Purpose:This Program opens a file, splits the lines up, adds the first 2 number pair together
# then organizes those numbers from gold, silver and bronze

#Open Up the file
f = open("input.txt","r")
#
outputFile = open("output.txt", "w+")

playerScores= f.read().split("\n")

playerOneScore = (float(playerScores[0]) + float(playerScores[1]))
playerTwoScore = (float(playerScores[2]) + float(playerScores[3]))
playerThreeScore = (float(playerScores[4]) + float(playerScores[5]))


gold = max(playerOneScore, playerTwoScore, playerThreeScore)

bronze = min(playerOneScore, playerTwoScore, playerThreeScore)

outputFile.write('Gold: {:0.2f}\n'.format(gold))

if playerOneScore < gold and playerOneScore > bronze:
    outputFile.write('Silver: {:0.2f}\n'.format(playerOneScore))
elif playerTwoScore < gold and playerTwoScore > bronze:
    outputFile.write('Silver: {:0.2f}\n'.format(playerTwoScore))
elif playerThreeScore < gold and playerThreeScore > bronze:
    outputFile.write('Silver: {:0.2f}\n'.format(playerThreeScore))    

outputFile.write('Bronze: {:0.2f}\n'.format(bronze))

outputFile.close()
f.close()