# Approach #4 using * operand
# this operand proposes a change to iterable unpacking syntax
#allowing to specify a “catch-all” name which will be assigned a list of all items 
# not assigned to a “regular” name. 

def swaplist(list):
    start, *middle, end = list 
    list = [end, *middle, start]
    return list

# driver code
newlist = [12,35,9,56,24]
print(swaplist(newlist))