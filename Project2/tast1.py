# first opening input.txt file in read mode
# then creating output.txt file for storing the results
inputfile = open("input.txt", "r")
outputfile = open("output.txt", "w")

# traversing the input file line by line until end of file is reached
for line in inputfile:
# getting the three values in each line
    number, rotate_L_or_R, rotate_value = line.split()
    
    # first converting number to binary string form of 16 bits
    binary = format(int(number), '016b')
    
    # given rotation value may be very large therefore we need to use modulo operation
    # because after rotating 16 bits we obtain the same number
    # Therefore new_rotate_value = rotate_value mod 16
    new_rotate_value = int(rotate_value) % 16
    
    # then depending on whether left or right rotate we will do the required rotate operation
    if rotate_L_or_R == 'L': # left rotation
        new_binary = binary[new_rotate_value:] + binary[:new_rotate_value]
    elif rotate_L_or_R == 'R': # right rotation
        new_binary = binary[16 - new_rotate_value:] + binary[:16 - new_rotate_value]
    
    # converting the new binary number to decimal form
    new_number = int(new_binary, 2)
    
    # saving it to output file
    outputfile.write(str(new_number) + '\n')

# closing the files
inputfile.close()
outputfile.close()