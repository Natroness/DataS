#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'first_non_repeating_character' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
"We can use a queue to tack the order of characters that could be unique. We can also use a dictionary to count how many times each character appears."

from collections import deque

def first_non_repeating_character(s):
    #creating an empty dictionary to count how many times  each character appears.
    count = {}
    #Creating an empty queue to store characters along with their index.
    #each character we add wil look like (character,index)
    q = deque()
    #iterating through s one character at a time 
    #also enumerate gives us both index and character
    for i, ch in enumerate(s):
        #if its not in dictionary ,start with 0 and then 1
        count[ch] = count.get(ch,0)+1
        #adding character and its index into the queue 
        q.append((ch,i))
        #checking from the left if the count is more than 1
        #if it has more than 1 it means that it has already been repeated 
        while q and count[q[0][0]]>1:
            q.popleft()
            
    #if queue not empty,returning the index of front  element
    return q[0][1] if q else -1 
    

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            s = ast.literal_eval(input_str)

            result = first_non_repeating_character(s)

            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")
    outfile.close()