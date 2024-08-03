# Lists
#Python Lists are ordered collections of data just like arrays in other programming languages. 
# It allows different types of elements in the list. The implementation of Python List is similar to Vectors in C++ or ArrayList in JAVA. 
# The costly operation is inserting or deleting the 
# element from the beginning of the List as all the elements are needed to be shifted. 
# Insertion and deletion at the end of the list can also become costly in the case where the preallocated memory becomes full.

# Creation python list
List = [1, 2, 3, "GFG", 2.3]
print(List)
#List elements can be accessed by the assigned index. 
# In python starting index of the list, a sequence is 0 and the ending index is (if N elements are there) N-1.

# python list operations

#creating  list with
# the use of multiple values
List1 = ["geeks", "for","geeks"]
print("\nList containing multiple values: ")
print(List1)

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['geeks' 'for'],[ 'geeks']]
print("\nMulti-dimensional List: ")
print(List2)

# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list 
print(List[-1])

#print the third last element of List
print(list[-3])



