def string_compare(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    lmin = min(l1, l2)
    
    for i in range(lmin):
        str_1 = ord(str1[i])
        str_2 = ord(str2[i])
      
        if str_1!= str_2:
            return 0

    if l1!=l2:
      return 0
    else:
       return 1
   
string1 = 'Geeksforgeeks'
string2 = 'practice'
string3 = 'geeks'
string4 = 'geeks'

print("Comparing", string1, "and", string2, ":" ,string_compare(string1,string2))
print("Comparing", string3, "and", string4, ":" ,string_compare(string1,string2))
print("Comparing", string3, "and", string4, ":" ,string_compare(string1,string2))
    