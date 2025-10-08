"palindrome Problem"
#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_palindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#

def is_palindrome(s):
    #converting string to lowercase for uniform comparison
    s = s.lower()
    #right pointer should be less than the len because its index
    left, right = 0, len(s)-1

    while left < right:
        
        #compare lowercase character first
        if s[left]!= s[right]: 
            return False
    #lets try moving the pointer after if condition
        left += 1
        right -= 1
    return True
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    arr = ast.literal_eval(input_data)

    result = is_palindrome(arr)
    print(result)