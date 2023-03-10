from mydata import l

def insertion_sort(A):
    if len(A) <= 1:
        return A
    
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1 #immediate left
        while j >=0 and key < A[j]:
            A[j + 1] = A[j]
            j = j - 1 #aarko left

        A[j + 1] = key

    return A
print(insertion_sort(l))