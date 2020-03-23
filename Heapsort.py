def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)

arr = [ 12, 11, 13, 5, 6, 7]
# heapSort(arr)
n = len(arr)

#heapify(arr, n, 6)

# Build a maxheap.
for i in range(n, -1, -1):
    heapify(arr, n, i)

