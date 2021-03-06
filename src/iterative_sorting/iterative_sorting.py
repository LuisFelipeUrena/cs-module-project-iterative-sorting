# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    if len(arr) == 0:
        return arr
    
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # if arr[smallest_index] < arr[smallest_index + 1]:
        #     arr[smallest_index] , arr[smallest_index + 1] = arr[smallest_index + 1] , arr[smallest_index]
        for j in range(smallest_index + 1 , len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i] , arr[smallest_index] = arr[smallest_index] , arr[i]    

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    if len(arr) == 0:
        return arr
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # if max is none, find the max value in the array and assign it
    if maximum is None:
        maximum = max(arr)
    # initialize a list of 0 with max len of the maximum
    helper = [0] * maximum
    # we loop tru the loop tru the list
    for i in arr:
        count = arr.count(i)
        helper.insert(i,count)
        # count instances of each number in the list
        # append it to the lists of 0's
    for i, v in enumerate(helper):
        # loop thru the list, starting at the leftmost index
        # and make the item next to the traversing index the sum 
        # of the traversing item and the item to its right
        helper[i + 1] = helper[i] + helper[i + 1]
         
    


    return arr
