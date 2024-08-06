def searchnum(arr,n,key):
    for i in range(n):
        if(arr[i]==key):
            
            return i
        
    return -1
        
#  driver code 
if __name__ == '__main__':
    arr = [23,34,45,56,67,78]
    key = 56
    n = len(arr)
    
    index = searchnum(arr,n,key)
    if index!= -1:
        print('element found at  '+ str(index+1))
    else:
        print("element not found")