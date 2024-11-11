def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        # find the most to the rightmost pos, remove the right most pos from the loop and repeat
        for j in range(0, n-i-1):        # after found the most, move to right-sorted, decrease the count
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break
    return arr

arr = [64,34,25,12,22,11,90]
print("Unsorted array:", arr)
sorted_arr = bubbleSort(arr)
print("Sorted array:", sorted_arr)