# Reverse Polish Notation Calculator
# This program helps you to calculate simple mathematical equations using Reverse Polish Notation
# Programming began circa September 2021
# A program by Tyler Serio
# Python version 3.9.5
# Works on Windows 10

# Import
import os
import math
from collections import deque

# Define operators
operators = ("+", "add", "-", "sub",  "x", "*", "mult", "/", "div", "%", "mod", "^", "pow", "ac", "p", "pop", "s", "swap", "ms", "mr", "mc", "sqrt", "m+", "mplus", "madd", "m-", "mmin", "msub", "m*", "mmult", "m/", "mdiv")

# Begin the calculator
stack = deque([0, 0, 0, 0, 0])
stored = 0
calculator = 1
while calculator == 1:
    # Calculator display
    print("Reverse Polish Notation Calculator")
    print("Type 'help' and press 'enter' for instructions.")
    print("----------------------------------")
    print(">                              " + str(stack[3]))
    print(">                              " + str(stack[2]))
    print(">                              " + str(stack[1]))
    print(">                              " + str(stack[0]))
    stackinput = (input(">                              "))

    # Help menu input
    if stackinput == "help":
        stack = deque([0, 0, 0, 0, 0])
        helping = 1
        while helping == 1:
            # Help menu display
            os.system("cls")
            print("Reverse Polish Notation Calculator")
            print("----------------------------------")
            print("This is a basic RPN (Reverse Polish Notation) calculator.")
            print("It supports addition, subtraction, multiplication, division, modulo, and exponentiation, and other functions.")
            print("To add a number to the stack, type the number and press 'enter'.")
            print("Operations are performed on the bottom two numbers of the stack.")
            print("")
            print("Operations:")
            print("Addition: Type '+' or 'add' and then press 'enter'.")
            print("Subtraction: Type '-' or 'sub' and then press 'enter'.")
            print("Multiplication: Type 'x' or '*' or 'mult' and then press 'enter'.")
            print("Division: Type '/' or 'div' and then press 'enter'.")
            print("Modulo: Type '%' or 'mod' and then press 'enter'.")
            print("Exponentiation: Type '^' or 'pow' and then press 'enter'.")
            print("Square Root: Type 'sqrt' and then press 'enter'.")
            print("To clear the entire stack type 'ac' and then press 'enter'.")
            print("To clear the first line of the stack and shift the stack down type 'p' or 'pop' and then press 'enter'.")
            print("To swap the last two entered lines of the stack type 's' or 'swap' and then press 'enter'.")
            print("To store the first line of the stack in memory for later use type 'ms' and then press 'enter'.")
            print("To recall a stored number from memory and insert it into the stack type 'mr' and then press 'enter'.")
            print("To add the first number of the stack to the stored number type 'm+' or 'mplus' or 'madd' and then press 'enter'.")
            print("To subtract the first number of the stack from the stored number type 'm-' or 'mmin' or 'msub' and then press 'enter'.")
            print("To multiply the stored number by the first number of the stack type 'm*' or 'mmult' and then press 'enter'." )
            print("To divide the stored number by the first number of the stack type 'm/' or 'mdiv' and then press 'enter'.")
            print("To reset memory to 0 type 'mc' and then press 'enter'.")
            print("")
            print("Type '0' and press 'enter' to return to the calculator.")
            selection = input(">")
            if selection == "0":
                helping = 0
                os.system("cls")
                break
            
    # Operator iput
    if stackinput in operators:
        # Swap
        if stackinput == "s" or stackinput == "swap":
            x = stack.popleft()
            y = stack.popleft()
            stack.appendleft(x)
            stack.appendleft(y)

        # Pop
        if stackinput == "p" or stackinput == "pop":
            stack.popleft()
            stack.append(0)

        # Clear
        if stackinput == "ac":
            stack.clear()
            stack = deque([0, 0, 0, 0, 0])

        # Addition
        if stackinput == "+" or stackinput == "add":
            answer = float(stack[1]) + float(stack[0])
            stack.popleft()
            stack.popleft()
            stack.appendleft(answer)
            stack.append(0)

        # Subtraction
        if stackinput == "-" or stackinput == "sub":
            answer = float(stack[1]) - float(stack[0])
            stack.popleft()
            stack.popleft()
            stack.appendleft(answer)
            stack.append(0)

        # Multiplication
        if stackinput == "x" or stackinput == "*" or stackinput == "mult":
            answer = float(stack[1]) * float(stack[0])
            stack.popleft()
            stack.popleft()
            stack.appendleft(answer)
            stack.append(0)

        # Division
        if stackinput == "/" or stackinput == "div":
            answer = float(stack[1]) / float(stack[0])
            stack.popleft()
            stack.popleft()
            stack.appendleft(answer)
            stack.append(0)

        # Exponentiation
        if stackinput == "^" or stackinput == "pow":
            answer = float(stack[1]) ** float(stack[0])
            stack.popleft()
            stack.popleft()
            stack.appendleft(answer)
            stack.append(0)

        # Modulus
        if stackinput == "%" or stackinput == "mod":
            answer = float(stack[1]) % float(stack[0])
            stack.popleft()
            stack.popleft()
            stack.appendleft(answer)
            stack.append(0)

        # Square root
        if stackinput == "sqrt":
            answer = math.sqrt(stack.popleft())
            stack.appendleft(answer)

        # Store
        if stackinput == "ms":
            stored = stack.popleft()
            stack.append(0)

        # Recall
        if stackinput == "mr":
            stack.appendleft(stored)

        # Memory clear
        if stackinput == "mc":
            stored = 0

        # Memory plus
        if stackinput == "m+" or stackinput == "mplus" or stackinput == "madd":
            stored = stored + stack.popleft()
            stack.append(0)
            
        # Memory minus
        if stackinput == "m-" or stackinput == "mmin" or stackinput == "msub":
            stored = stored - stack.popleft()
            stack.append(0)
            
        # Memory multiply
        if stackinput == "m*" or stackinput == "mmult":
            stored = stored * stack.popleft()
            stack.append(0)
            
        # Memory divide
        if stackinput == "m/" or stackinput == "mdiv":
            stored = stored / stack.popleft()
            stack.append(0)
    else:
        # Remove the top element of the top of the stack
        stack.pop()
        try:
            # Add the number input to the bottom of the stack
            stack.appendleft(float(stackinput))
        except ValueError:
            # If the number input is not proper, add another 0 to the bottom of the stack
            stack.appendleft(0)
