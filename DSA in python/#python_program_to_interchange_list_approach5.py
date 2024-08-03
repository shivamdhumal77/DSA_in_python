#Approach #5: Swap the first and last elements is to use the inbuilt function list.pop(). Pop the first element and store it in a variable. Similarly, 
#pop the last element and store it in another variable. Now insert the two popped element at each other’s 
#original position. 

# python3 program to swap first
# and last element of a list

def swaplist(list):
    first = list.pop(0)
    last = list.pop(-1)
    
    list.insert(0, last)
    list.append(first)
    
    return list

# driver code
newlist = [12,35,9,56,24]
print(swaplist(newlist))
