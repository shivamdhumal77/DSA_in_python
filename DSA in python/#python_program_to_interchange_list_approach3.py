#Approach #3: Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get, 
#and unpack those elements with first and last element in that list.
#Now, the First and last values in that list are swapped. 

# python program to swap first 
def swaplist(list):
    # storing the first and last element
    # as a pair in a tuple variable get
    get = list[-1], list[0]
    list[0], list[-1] = get
    
    return list

# driver code
newlist = [12,35,9,56,24]
print(swaplist(newlist))