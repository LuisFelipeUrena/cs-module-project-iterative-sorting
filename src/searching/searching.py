def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1    
   



      # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid  = (high + low) // 2

        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            high = mid - 1
        
        if target > arr[mid]:
            low = mid + 1 

    return -1        





    # return -1  # not found
