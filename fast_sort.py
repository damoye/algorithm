def fast_sort(A, p, q):
    if q - p <= 1:
        return
    k, i = p, p + 1
    while i != q:
        if A[i] < A[k]:
            A[k+1], A[i] = A[i], A[k+1]
            A[k], A[k+1] = A[k+1], A[k]
            k += 1
        i += 1
    fast_sort(A, p, k)
    fast_sort(A, k + 1, q)
