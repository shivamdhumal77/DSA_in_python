# Find the peak element using recursive Binary Search
# Using Binary Search, check if the middle element is the peak element or not. If the middle element is not the peak element, then check if the element on the right side is greater than the middle element then there
# is always a peak element on the right side. 
# If the element on the left side is greater than the middle element then there is always a peak element on the left side. 


def findpeak(arr, n):
    
    if(n==1):
        return 0
    if (arr[0]>=arr[1]):
        return 0
    if (arr[n-1]>=arr[n-2]):
        return n-1 
    
    for i in range(1, n-1):
        if (arr[i]>=arr[i-1]and arr[i]>=arr[i+1]):
         return i 
    
    
    # driver mode 
    arr = [1,2,20,4,1,0]
    n = len(arr)
    print("Index of a peak point id ", findPeak(arr,n))