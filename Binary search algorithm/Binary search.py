
#example for binary search
def binary_search(arr, target):
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        middle = (lower + upper) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1

    return -1  # Target element not found

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
result = binary_search(arr, target)
print("Element found at index:", result)  # Output: Element found at index: 5

''' 
In this example, the binary_search() function performs a binary search 
on the sorted array arr 
to find the target element target. If the target element is found,
it returns the index of the element. Otherwise,
 it returns -1 to indicate that the target element is not present in the array.
''' 
''' 
Note that the Binary Search Algorithm requires the array to be 
sorted beforehand for accurate results.
''' 