# Workshop 1 - Part 1 - Step 1

# Requirements:
    # Write a basic Python "calculator". 
    # It should accept 3 pieces of input from the user: a string that's one of "x", "+", "-", or "/" (an operation), an integer (parameter A), and another integer (parameter B). 
    # It should then emit the result of performing the operation on A and B. 
    # For example, if your application asks the user for an operation and 2 numbers, and the user enters "+", "1", "2", then the application should output "3".
    # If the user supplied "/", "5", "2", the application should output "2.5". 
    # If the user supplied "x", "5", "0", the application should output 0.

operation = input ('''
Enter an operation to perform:
+ to add
- to subtract
* to multiply
/ to divide )
''') # Variable to store user operation

param1 = int(input('Enter first integer: ')) # we need to tell python that the input is an integer, otherwise it'll fail with an error.
param2 = int(input('Enter second integer: '))

if operation == '+':
    print(param1 + param2)

elif operation == '-':
    print(param1 - param2)

elif operation == '*':
    print(param1 * param2)

elif operation == '/':
    print(param1 / param2)

else:
    print('You have been a numpty and entered an invalid operation.') # Validation to make sure the user doesn't enter something random. 