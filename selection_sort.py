def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]: # If the "current minimum" element is greater than the "current element"
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swap the "current element" with the "minimum element"
    return arr

A = [64, 25, 12, 22, 11]
sorted_A = selection_sort(A)
print("Sorted array:", *sorted_A) # The print statement is simplified using the * operator to unpack the sorted array