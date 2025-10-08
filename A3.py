#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'two_sum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER target
#
"For this I think we should use the two pointer method , one at the beginning and one at the end.We should return the index+1 meaning the pointer+1. For this  We can run nested for loop."
def two_sum(numbers, target):
    # Write your code here
    #starting pointer
    left = 0
    #ending pointer
    right = len(numbers)-1
    
    while left<right:
        #caclulating the current sum 
        sum = numbers[left] + numbers[right]
        
        #checking if the returning sum is the target we need
        if sum == target:
            #if the condition is true returning the index+1
            return [left +1 , right +1 ]
            
        elif sum <target:
            #sum too small moving left pointer to right 
            left +=1
        else:
            #if sum is too large moving right pointer towards left. 
            right -=1
            
            
            
    return
            
    

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    for line in input_data:
        input_list = ast.literal_eval(line)
        nums = input_list[0]
        target = input_list[1]

        result = two_sum(nums, target)
        outfile.write(str(result) + '\n')
    outfile.close()