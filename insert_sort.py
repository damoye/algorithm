def insert_sort(A):
    i = 1
    while i != len(A):
        j = i
        while j != 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1
