#You are planning a special event where each attendee has a unique registration number. These numbers are listed in the provided array attendees,
#but they are currently out of order.
#At the event, attendees will walk on stage one by one following this special reveal process:
#The person at the front of the line walks on stage (this number is revealed).
#If there are still people left in line, the next person in front moves to the back of the line.
#Steps 1 and 2 repeat until everyone has walked on stage.
#Your task is to rearrange the attendees list before the process starts so that the attendees walk on stage by registration number in increasing order.

#Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, such that when the attendees follow the above reveal process they walk on stage from smallest registration number to largest registration number.

#Example Usage:


def reveal_attendee_list_in_order(attendees):
  #for this i think we can use array and then we add the value in the stack but for the problem,,
  #I would use sort() function in the python, first in -> the stack, then i would put 0->2nd one, 
  # i would put 2nd element in the third and i would put 0 for each odd element number
  #for that i would use a for loop
  #iterate through each
  #once the everythiing  is inside i would come back and put variables instead of 0.
#this sorts the given array
    #attendees.sort()
#declare the returning array
    #arr=[]

  # in for loop
    #for i in range(0,len(attendees)-1):
     #   if i % 2 ==0:
      #      arr[i]=attendees[]


#I think this method wont work as it would be hard to put the 
#array in circular order
#Lets try que

#What i am thinking is may be we can sort the given array
#Then create a queue
#may be we can add everything in a queue but we put the greater ones in the end
    #importing queue
    from collections import deque
#lets try this method 
    #sorting the given array
    attendees.sort()

    #creating queue
    dq = deque()

    #stimulating backward so that we put last in the back
    for num in reversed(attendees):
        #IF queue has number we pop it and put it in the back
        if dq:
            #if que has number it pops and put it in the front 
            dq.appendleft(dq.pop())
        #we add number in the first
        dq.appendleft(num)

    return list(dq)





  

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000])) 





#Example Output:

#[2,13,3,11,5,17,7]
#[1,1000] "