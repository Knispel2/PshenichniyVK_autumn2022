import ctypes


def c_matmult(a, b):
    libmatmult = ctypes.CDLL("./07/mult.so")
    dima = len(a) * len(a)
    dimb = len(b) * len(b)
    array_a = ctypes.c_float * dima
    array_b = ctypes.c_float * dimb
    array_c = ctypes.c_float * dima
    suma = array_a()
    sumb = array_b()
    sumc = array_c()
    inda = 0
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            suma[inda] = a[i][j]
            inda = inda + 1
        indb = 0
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            sumb[indb] = b[i][j]
            indb = indb + 1
    libmatmult.multMatrixSqBad(ctypes.byref(suma), ctypes.byref(sumb), ctypes.byref(sumc), len(a));
    res = [[0 for _ in range(len(a))] for _ in range(len(a))]
    indc = 0
    for i in range(0, len(sumc)):
        res[indc][i % len(a)] = sumc[i]
        if i % len(a) == len(a) - 1:
            indc = indc + 1
    return res


def matmult(a,b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]
