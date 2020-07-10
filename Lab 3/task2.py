# Author: Brandon London
# Date: 06/18/2020
# Version: 1
#===============================================================================
# #In each line of the input file (filename: input.txt), there are exactly 6 numbers (separated by whitespaces). The
# first 3 values are the 𝒙-, 𝒚-, and 𝒛-coordinates of the first point; the rest 3 values are the 𝒙-, 𝒚-, and 𝒛-coordinates
# of the second point. You cannot assume (or guess) the number of lines in the input file. No matter how many
# lines are in the input file, your program should process all of them. There may be empty lines at the beginning,
# in the middle, and/or at the end of the input file, and your program should smartly skip those empty lines. Please
# refer to the sample input files to better understand the input file format.
# After reading in the input values from the input file, your program should calculate the distance between the two
# points in each line and write the result to the output file (filename: output.txt), one result per line. Keep 2
# decimal places in your results.
#===============================================================================

#import math for the square root
import math
#import re for regular expressions
import re
#Open Up the file
f = open("input.txt","r")
# create and open the output file with write capabilities
outputFile = open("output.txt", "w+")
#for each line in the file do the following
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
        distance = math.sqrt(((xOne - xTwo) ** 2) +((yOne - yTwo) ** 2) + ((zOne - zTwo) ** 2))
        #write calculation to the output file and then repeat for the remaining lines
        outputFile.write('{:0.2f}\n'.format(distance))
f.close()
outputFile.close()
#===============================================================================