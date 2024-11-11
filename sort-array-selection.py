def selectionSort(arr):
    
    n = len(arr)  # compare and set the lowest to the leftmost, remove leftmost pos and repeat
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr            

arr = [12,11,35,9,56,2,6,77,1]
print("The unsorted array is: ", arr)
sortedArr = selectionSort(arr)
print("The sorted array is: ", sortedArr)


#optimized code, set i to  min_index, if arr[j] lower than arr[i], update min_index--no need to swap
#when the current iteration ended, check min_index if in right position, swap if not

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i  # Assume the current position is the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the index of the minimum element
        
        # If the minimum element is not already at index `i`, swap it
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [12, 11, 35, 9, 56, 2, 6, 77, 1]
print("The unsorted array is: ", arr)
sortedArr = selectionSort(arr)
print("The sorted array is: ", sortedArr)