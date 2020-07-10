# Author: Brandon London
# Date: 06/18/2020
# Version: 1
# 1) Read in the 4 values from the input file.
#2) Based on the input values, calculate after how many years, the population of town A will be greater than (or
#equal to) town B.
#3) Show the number of years needed (calculated in the previous step) to the standard console. There is no output
#file in this program.
#open input file
f = open("input.txt","r")
# from the input put the data into a list seperated by new lines
townValue = f.read().split("\n")
townOnePop = int(townValue[0])
townOneRate = float(townValue[1])
townTwoPop = int(townValue[2])
townTwoRate = float(townValue[3])
years = 0

print(townOnePop)
print(townTwoPop)
#while town one population is less keep going
while townOnePop < townTwoPop:
    #calculate both populations until town one is bigger
    townOnePop = (townOnePop * (1 + townOneRate))
    townTwoPop = (townTwoPop * (1 + townTwoRate))
    #keep track of ears
    years = 1 + years
#print out number of years
print("Number of years: " + str(years))
#close file
f.close()