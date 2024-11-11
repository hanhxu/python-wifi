def insertionSort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # The current element to be inserted into the sorted part
        j = i - 1  # Start comparing with the element before 'i'
        
        # Move elements of arr[0..i-1] that are greater than 'key' to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        
        # Place the key at the correct position, if key value lower than all values on the left, j=-1, then arr[0]=key
        arr[j + 1] = key
    
    return arr


arr = [12, 11, 35, 9, 56, 2, 6, 77, 1]
print("The unsorted array is:", arr)

sortedArr = insertionSort(arr)
print("The sorted array is:", sortedArr)