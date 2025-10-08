#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_valid' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#
"What I am thinking rn is create a stack and put a condition that if we find the opening we put it in the stack and if we dont find the closing we dont pop"
"At the end we check if we have anything in the stack if yes we would return the false else we would return True."
"To start may be create stack and pair of brackets - run loop for characters - check if opening bracket- if yes put in the stack. 2nd would be if stack is empty or no if not the we check if its closing bracket. IF its closing bracket then pop from cheking the previous pair of closing and opening bracket. at the end we check if there is empty stack or no if empty true or else False"


def is_valid(s):
    
    # Write your code here
    #creating stack
    stacks=[]
    #creating Pairs
    pairs = {')':'(',']':'[','}':'{'}
    
    #running for loop for characters in S
    
    for ch in s:
    #checking if its the opening bracket
        if ch in "({[":
        #adding in stack if opening 
            stacks.append(ch)
    #checking if its in the closing bracket     
        elif ch in ")]}":
            if not stacks or stacks[-1] != pairs[ch]:
                return False
            stacks.pop()
        
    return not stacks
        
    

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            s = ast.literal_eval(input_str)

            result = is_valid(s)

            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")
    outfile.close()