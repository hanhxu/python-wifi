# Here’s an outline of the steps in Heap Sort:

# Build a max heap: Rearrange the array into a binary heap.
# Swap the root (largest element) with the last element: This places the largest element at its correct position.
# Reduce the heap size by one: Ignore the last element (which is now in its correct position) and heapify the remaining elements.
# Repeat the process: Continue swapping and heapifying the rest of the array until the entire array is sorted.
# heapify(arr, n, i):
# This function ensures that the subtree rooted at index i is a valid heap.
# It compares the root with its left and right children. If either child is larger than the root, it swaps the root with the larger child and recursively ensures that the heap property is maintained.
# heap_sort(arr):
# First, it builds the heap starting from the last non-leaf node (n // 2 - 1).
# After the heap is built, it repeatedly swaps the root (largest element) with the last element, reduces the heap size by 1, and calls heapify on the root to restore the heap property.

def heapify(arr, n, i):
    largest = i                                     # initialize largest as root
    left = 2 * i + 1                                # left child index
    right = 2 * i + 2                               # right child index
    
    # check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    # check if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right
    # if largest is not root, swap and continue heapifying the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]      # Swap       
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)             
def heap_sort(arr):
    n = len(arr) 
    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # one by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap the root--largest element with the last element
        heapify(arr, i, 0)   # heapify the root of the tree
        
arr = [12, 11, 13, 5, 6, 7]
print("Unsorted array is:", arr)
heap_sort(arr)
print("Sorted array is:", arr)