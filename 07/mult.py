import ctypes


def c_matmult(a_arg, b_arg):
    libmatmult = ctypes.CDLL("./07/mult.so")
    dima = len(a_arg) * len(a_arg)
    dimb = len(b_arg) * len(b_arg)
    array_a = ctypes.c_float * dima
    array_b = ctypes.c_float * dimb
    array_c = ctypes.c_float * dima
    suma = array_a()
    sumb = array_b()
    sumc = array_c()
    inda = 0
    indb = 0
    for i in enumerate(a_arg):
        for j in enumerate(a_arg[i]):
            suma[inda] = a_arg[i][j]
            inda = inda + 1
    for i in enumerate(b_arg):
        for j in enumerate(b_arg[i]):
            sumb[indb] = b_arg[i][j]
            indb = indb + 1
    libmatmult.multMatrixSqBad(ctypes.byref(suma),
                               ctypes.byref(sumb),
                               ctypes.byref(sumc),
                               len(a_arg))
    res = [[0 for _ in enumerate(a_arg)]
           for _ in enumerate(a_arg)]
    indc = 0
    for i in enumerate(sumc):
        res[indc][i % len(a_arg)] = sumc[i]
        if i % len(a_arg) == len(a_arg) - 1:
            indc = indc + 1
    return res


def matmult(a_arg, b_arg):
    zip_b = zip(*b_arg)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b
                 in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a_arg]
