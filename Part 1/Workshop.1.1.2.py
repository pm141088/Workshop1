# Workshop 1 - Part 1 - Step 2

# Next process the following file: Link
# Each line contains a calculation statements prefixed by "calc":
# Compute the value of each line using the code from step 1
# Add up the results from all the lines and send the results to the trainer

# Hint 1: For reading the lines from the file you may want to use file.read().splitlines() to build a list of lines.
# Hint 2: you may want to use string.split() to break up the parts of each calc line.


with open("step_2.txt",'r') as f: # calling Python built-in function to open file in read only mode
    text_string = f.read()
    # f.close() # Not required when using this function
    #print(text_string)

mylist = text_string.splitlines() # The splitlines() method splits a string into a list. The splitting is done at line breaks.
print(mylist) #['calc / 69 78', 'calc x 16 38', 'calc + 23 57',

total = [] # new variable to hold empty list to begin with, then we will append to this list.

for x in mylist:
    
    calclist = x.split() # The split() method splits a string into a list.
    print(calclist) # '0: calc, 1: /, 2: 69, 3: 78'
    calc = calclist[0] # calc
    operator = calclist[1] # /
    param1 = int(calclist[2]) # 69
    param2 = int(calclist[3]) # 78

    if operator == '+':
        print(param1 + param2)
        total.append(param1 + param2) # Add value to total variable so we can add up at the end

    elif operator == '-':
        print(param1 - param2)
        total.append(param1 - param2)

    elif operator == '*' or operator == 'x':
        print(param1 * param2)
        total.append(param1 * param2)

    elif operator == '/':
        print(param1 / param2)
        total.append(param1 / param2)
    
print(total) 

print(sum(total)) # calling sum method to add all the elements in the total list.