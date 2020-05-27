# Workshop 1 - Part 1 - Step 3

# Next navigate the following file: Link
# This has goto statements like the following: goto 27
# This means go to line 27 in the file and read the statement there. Please note that calc and goto statements can be combined like so: goto calc / 27 9
# This is equivalent to goto 3.
# For simplicity assume that we cannot nest calc statements, decimals are rounded down and out of bounds gotos (i.e. invalid line numbers) do not occur.

# Starting from line 1, use the rules above to navigate the document, stopping when you've hit a statement you’ve seen once before (they are allowed to be from different lines!).
# When finished please send the statement and line number the code has stopped on to a tutor.

memory = []
line_count = 0

# New function to check for duplicate entries in memory
def checkForDupes(memory):
    for item in memory:
        if memory.count(item) > 1:
            return True
    return False

with open("step_4.txt",'r') as f:
    #text_string = f.read()
    lines = f.readlines()

with open("step_4.txt",'r') as f:    
    for line in f:
            line_count = line_count + 1

result = checkForDupes(memory)

i = 0 # We need to start in Line 1 which equals index 0
while result == False:

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
        line = lines[i-1]
    
        result = checkForDupes(memory) # Call the function to check for dupes!

        if result == True: 
            print('Duplicate found in memory!')
            print('Line Number: ', i)
        else: 
            print('No duplicates found in memory')

    elif linesplit[0] == 'goto':
        i = int(linesplit[1])
        line = lines[i-1] # we have to subtract 1 to get to the correct line number in the file as Python indexes from 0 and hte first line of a file is line 1
        #memory.append(line) # add current line to memory

        result = checkForDupes(memory)

        if result == True: 
            print('Duplicate found in memory!')
            print('Line Number: ', i)
        else: 
            print('No duplicates found in memory')
    
    elif linesplit[0] == 'replace':
        i = int(linesplit[1])
        line = lines[i-1] # we have to subtract 1 to get to the correct line number in the file as Python indexes from 0 and hte first line of a file is line 1
        #memory.append(line) # add current line to memory

        result = checkForDupes(memory)

        if result == True: 
            print('Duplicate found in memory!')
            print('Line Number: ', i)
        else: 
            print('No duplicates found in memory')
    
    elif linesplit[0] == 'remove':
        i = int(linesplit[1])
        line = lines[i-1] # we have to subtract 1 to get to the correct line number in the file as Python indexes from 0 and hte first line of a file is line 1
        #memory.append(line) # add current line to memory

        result = checkForDupes(memory)

        if result == True: 
            print('Duplicate found in memory!')
            print('Line Number: ', i)
        else: 
            print('No duplicates found in memory')    