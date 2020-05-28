# Workshop 1 - Part 1 - Step 4

# Next navigate the following file: Link
# This has goto statements like the following: goto 27
# This means go to line 27 in the file and read the statement there. Please note that calc and goto statements can be combined like so: goto calc / 27 9
# This is equivalent to goto 3.
# For simplicity assume that we cannot nest calc statements, decimals are rounded down and out of bounds gotos (i.e. invalid line numbers) do not occur.

# The goal is to process the file, starting from line 1, stopping when you’ve hit a statement you’ve seen before or manage to jump outside the file by a goto.

memory = []
line_count = 0
filename = 'C:\Work\git\Workshop1\Part_1\step_4.txt' 

# FUNCTIONS
# 1. function to check for duplicate entries in memory
def checkForDupes(memory):
    for item in memory:
        if memory.count(item) > 1: # The count() method returns the number of elements with the specified value.
            return True
    return False

with open(filename,'r') as f: # read all lines and store into a variable called lines
    #text_string = f.read()
    lines = f.readlines()
    line_count = len(lines)


result = checkForDupes(memory)

i = 0 # We need to start in Line 1 which equals index 0
while result == False: # While loop 

    if i == 0: 
        line = lines[i]
    else:
        line = lines[i-1]
    #line = lines[i] # New variable created to start at line 1 in the file
    print(line) # goto 1236
    memory.append(line) # add current line to memory

    linesplit = line.split() # splitting line into a list
    print(linesplit) # ['goto', '1236']

    # Variables required to reset the values as it loops between the lines 
    operator = ''
    param1 = ''
    param2 = ''
    output = ''

    if linesplit[1] == 'calc': # Look directly at index 1 in the file, if we find the string: calc then we need to perfrom a calculation else its just a goto statement.
        operator = linesplit[2] 
        param1 = int(linesplit[3])
        param2 = int(linesplit[4])

        if operator == '+': output = (param1 + param2)
        elif operator == '-': output = (param1 - param2)
        elif operator == '*' or operator == 'x': output = (param1 * param2)
        elif operator == '/': output = (param1 / param2)

        i = int(output)

        if i <= line_count:

            line = lines[i-1]
        
            result = checkForDupes(memory) # Call the function to check for dupes!

            if result == True: 
                print('Duplicate found in memory!')
                print('Line Number: ', i)
            else: 
                print('No duplicates found in memory')
        else:
            print('Index out of range') # Index out of range means that the index you are trying to access does not exist!
            break

    elif linesplit[0] == 'goto':
        i = int(linesplit[1])
        line = lines[i-1] # we have to subtract 1 to get to the correct line number in the file as Python indexes from 0 and hte first line of a file is line 1
        #memory.append(line) # add current line to memory

        if i <= line_count:

            result = checkForDupes(memory)

            if result == True: 
                print('Duplicate found in memory!')
                print('Line Number: ', i)
            else: 
                print('No duplicates found in memory')
        else:
            print('Index out of range') # The line number does not exist!
            break
    
    elif linesplit[0] == 'replace':
        x = int(linesplit[1]) - 1
        y = int(linesplit[2]) - 1
        #line_1 = lines[x-1] 
        #line_2 = lines[y-1] 

        if x > len(lines) or y > len(lines):
            print("cannot replace line {0} with line {1}".format(x, y))
        else:
            print("replace: {0} with: {1}".format(lines[x], lines[y]))
            #lines[x] = lines[y]
            #print("new value {0}".format(lines[x]))

        result = checkForDupes(memory)

        if result == True: 
            print('Duplicate found in memory!')
            print('Line Number: ', i)
        else: 
            print('No duplicates found in memory')
    
    elif linesplit[0] == 'remove':
        i = int(linesplit[1])
        line = lines[i-1] # we have to subtract 1 to get to the correct line number in the file as Python indexes from 0 and hte first line of a file is line 1
        
        if i <= line_count:
        
            f = open('C:\Work\git\Workshop1\Part_1\step_4.txt', 'r') # open current file in readonly mode
            output = [] # new array called output
            remove_line = line # assign remove_line to the line which needs to be removed.

            for line in f: # for loop to read each line and append all lines to the output array that doesn't start with line stored in: remove_line
                if not line.startswith(remove_line):
                    output.append(line)
            f.close() # close the file

            f = open('C:\Work\git\Workshop1\Part_1\step_4.txt', 'w') # open the file again this time in write mode  
            f.writelines(output) # write the data saved in the output array to the same file
            f.close() # close the file!

            result = checkForDupes(memory)

            if result == True: 
                print('Duplicate found in memory!')
                print('Line Number: ', i)
            else: 
                print('No duplicates found in memory')    
        else:
            print('Index out of range') # The line number does not exist!
            break