#import math for the square root
import math
#import re for regular expressions
import re
#Open Up the file
distlist = []
f = open("input.txt","r")
# create and open the output file with write capabilities
outputFile = open("output.txt", "w+")
def calcDistance(xOne, xTwo, yOne, yTwo, zOne, zTwo):
    distance = math.sqrt(((xOne - xTwo) ** 2) +((yOne - yTwo) ** 2) + ((zOne - zTwo) ** 2))
    distlist.append(distance)
    return(distlist)
for line in f:
#use regular expression to substitute any whitespace with a single space
    coordinates = re.sub('\s+',' ',line)
    #split the line into a list by the single whitespace thats left
    coordinates = coordinates.split()
    #print out the list for confirmation and testing
    print(coordinates)
    #check and make sure the list have content if not skip
    if len(coordinates) == 0: 
        print("nothing here")
    else: 
    #of the list does have content, assign a number to the corresponding variable
        xOne = float(coordinates[0])
        yOne = float(coordinates[1])
        zOne = float(coordinates[2])
        xTwo = float(coordinates[3])
        yTwo = float(coordinates[4])
        zTwo = float(coordinates[5])
        #calculate the total distance
        calcDistance(xOne, xTwo, yOne, yTwo, zOne, zTwo)        
for dist in distlist:
    outputFile.write('{:0.2f}\n'.format(dist))
f.close()
outputFile.close()

