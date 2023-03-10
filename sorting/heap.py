from mydata import l

def min_heapify(A, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    # print(size)
    if l < size and A[l] < A[smallest]:
        smallest = l
        
    if r < size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        min_heapify(A, smallest, size)

def max_heapify(A, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < size and A[l] > A[largest]:
        largest = l
    if r < size and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, size)

def build_min_heap(A):
    for i in range(len(A) // 2, -1, -1):
        min_heapify(A, i, len(A))
    return A

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i, len(A))
    return A


def heap_sort(A):
    heap = build_max_heap(A)
    for size in range(len(A) - 1, -1, -1):
        heap[0], heap[size] = heap[size], heap[0]
        max_heapify(heap, 0, size)
    return heap

print(l)
print(heap_sort(l))