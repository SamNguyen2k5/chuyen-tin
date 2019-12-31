def func_a(a, k):
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j+1]) == k:
                return True

    return False

def func_b(a, k):
    n = len(a)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s == k:
                return True

    return False

def func_c(a, k):
    n = len(a)
    i, j = 0, 0
    s = 0
    while i < n:
        if s == k:
            return True
        
        if s > k or j == n:
            s -= a[i]
            i += 1

        if s < k and j != n:
            s += a[j]
            j += 1

    return False
