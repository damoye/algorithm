def merge_sort(A, temp, p, q):
    if q - p == 1:
        return
    mid = (p + q) / 2
    merge_sort(A, temp, p, mid)
    merge_sort(A, temp, mid, q)
    temp[p: mid] = A[p: mid]
    temp[mid: q] = A[mid: q]
    i, i1, i2 = p, p, mid
    while i != q:
        if i2 == q or i1 != mid and temp[i1] < temp[i2]:
            A[i] = temp[i1]
            i1 += 1
        else:
            A[i] = temp[i2]
            i2 += 1
        i += 1
