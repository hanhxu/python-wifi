# Quick Sort Steps:
# Pick a Pivot: Select an element from the array (usually the first, last, or middle element).
# Partitioning: Rearrange the elements in the array such that elements less than the pivot are on the left side, and elements greater than the pivot are on the right side.
# Recursion: Recursively apply the same process to the sub-arrays on the left and right of the pivot.

def quickSort(arr):
    
    if len(arr) <= 1:
        return arr
    
    # pick a pivot
    pivot = arr[len(arr) - 1]
    # Partition the array into two sub-arrays: one with elements smaller than the pivot,
    # and one with elements greater than the pivot.
    left = []
    right = []
    
    for i in range(len(arr)-1): # exclude the pivot element
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Recursively apply quicksort to the left and right sub-arrays
    return quickSort(left) + [pivot] + quickSort(right)

# Test the quickSort function
arr = [12, 11, 35, 9, 56, 2, 6, 77, 1]
print("Unsorted array:", arr)

sortedArr = quickSort(arr)
print("Sorted array:", sortedArr)