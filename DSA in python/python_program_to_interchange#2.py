#Approach #2: The last element of the list can be referred as list[-1]. Therefore, 
#we can simply swap list[0] with list[-1].

# python program to swap first
# and last element of a list 
# swap function

def swaplist(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return newlist

# driver code
newlist = [12,35,9,56,24]
print(swaplist(newlist))