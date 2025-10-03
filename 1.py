# understanding 
# output of that len(str(val))+1 
# output contains all integers from 1 to len(str(val))+1
# 

# For every index i from 0 to n - 1:

#     If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
#     If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].

# plan
# use a stack 
# 1. val == D 
# [DDD]
#  i

#  4

# []
# all nums available to use [123456789]
# stack = [123] 

def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    out = []
    curr = 1
    for i in range(len(arrival_pattern)):
        if arrival_pattern[i] == "I": 
            out.append(curr)
            curr += 1 
            while stack: 
                idx = stack.pop()
                out[idx] = curr
                curr += 1
        else: 
            stack.append(i) 
            out.append(-1)
  
    out.append(curr)
    curr += 1 
    while stack: 
        idx = stack.pop()
        out[idx] = curr
        curr += 1
    print(out)
    # return "".join(out)
      

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

# 123549876
# 4321