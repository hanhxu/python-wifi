# Divide: Split the array into two halves.
# Recursively sort: Sort each half.
# Merge: Merge the two sorted halves back together in sorted order.

def mergeSort(arr):
    
    if len(arr) > 1:
        midIndex = len(arr) // 2  # floor divide
        left_part = arr[:midIndex]
        right_part = arr[midIndex:]
        
        # recursively sort both arrays(left and right parts)
        mergeSort(left_part)
        mergeSort(right_part)
        
        # merge the two sorted halves array to the original
        # initialize index for sorted left--i, sorted right--j, and merged array--k
        i = j = k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        # if there is remaining elements from left_part, add them
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            
arr = [12, 11, 35, 9, 56, 2, 6, 77, 1]
print("The unsorted array is:", arr)
mergeSort(arr)
print("The sorted array is:", arr)
