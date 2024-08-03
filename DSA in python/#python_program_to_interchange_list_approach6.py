#Python program to interchange 
# first and last elements in a list

# How do you find the first and last items in a list Python?
#To find the first and last items in a list in Python, you can use indexing. 
# The first item in a list has index 0, and the last item has index -1. 
# Here’s how you can do it:

# Sample list
my_list1 = [1, 2, 3, 4, 5]
# Find the first item
first_item = my_list1[0]
# Find the last item
last_item = my_list1[-1]

#2 
#To switch the first and last characters in a string in Python, 
# you can use string slicing and concatenation. 
# Here’s how you can do it:

# Sample string
my_string = "hello"
# Switch first and last characters
new_string = my_string[-1] + my_string[1:-1] + my_string[0]

#3
#How to shift elements in a list in Python?
#To shift elements in a list in Python, 
# you can use slicing and concatenation. 
# Here’s how you can shift elements to the left by one position:

# Sample list
my_list2 = [1, 2, 3, 4, 5]
# Shift elements to the left by one position
shifted_list = my_list2[1:] + [my_list2[0]]

#To move an element to the end of a list in Python, 
# you can use list methods such as pop() and append(). 
# Here’s how you can move the first element to the end of the list:

# Sample list
my_list3 = [1, 2, 3, 4, 5]# Move the first element to the end
my_list3.append(my_list3.pop(0))

# How to swap characters in a list?
#To swap characters in a string in Python, you can convert the string to a list,
# perform the swap, and then convert the list back to a string. 
# Here’s how you can swap the first and last characters:

# Sample string
my_string4 = "hello"# Convert string to list
my_list0 = list(my_string4)# Swap first and last characters
my_list0[0], my_list0[-1] = my_list0[-1], my_list0[0]# Convert list back to string
new_string4 = "".join(my_list0)