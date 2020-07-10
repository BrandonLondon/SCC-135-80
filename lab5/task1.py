#Import math for calculation
import math
#Import re just because I want to kill mosquitos with a machine gun 
import re

#Create class/ object point 
class Point(object):
    #initalize with constructor and if values are null, assign them to 0
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    #create method that takes in current object and another object point
    def calcDistance(self, point):
        # building parts of the equation
        dx = self.x - point.x  # x1 - x2
        dy = self.y - point.y  # y1 - y2
        dz = self.z - point.z  # z1 - z2
        # calculate distance
        distance = math.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))
        # the above equation can also be written as below
        # distance = math.sqrt((dx*dx)+(dy*dy)+(dz*dy))
        # return the distance
        return distance
# entry point of the program
if __name__ == "__main__":
#explaination of the above Whenever the Python interpreter reads a source file, it does two things:
#it sets a few special variables like __name__, and then
#it executes all of the code found in the file.
    # list for storing distances
    distances = []
    # read the file
    f = open("input.txt","r")
        # read all lines
# for each line in the file do
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
                continue
        else:
            #Create point object 1 and assign the points into those objects
            p1 = Point(float(coordinates[0]), float(coordinates[1]), float(coordinates[2]))
            # create point object 2
            p2 = Point(float(coordinates[3]), float(coordinates[4]), float(coordinates[5]))
            # Calculate distance
            distances.append(p1.calcDistance(p2))
    with open("output.txt", "w") as outfile:
        for dist in distances:
            # rounding float value to 2 digits
            # and converting i to string
            # appending new line character
            outfile.write(str(round(dist, 2)) + "\n")