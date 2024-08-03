#Python program to interchange first and last elements in a list

# 1) find the length of the list and simply swap the first element (n-1)th element.


# python program to swap first
# and last element of a list

# swap function
def swaplist(newlist):
    size = len(newlist)
    
    # swapping
    temp=newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp
    
    return newlist

# driver code
newlist = [12,35,9,56,24]
print(swaplist(newlist))
