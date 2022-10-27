import time
import numpy
import mult

MAX = 50


def main():
    a_arg = [numpy.random.randint(0, 100, (n, n)).tolist()
             for n in range(MAX) if n != 0]
    b_arg = [numpy.random.randint(0, 100, (n, n)).tolist()
             for n in range(MAX) if n != 0]
    print("==== python ====")
    start_ts = time.time()
    res_py = [mult.matmult(x, y) for x, y in zip(a_arg, b_arg)]
    end_ts = time.time()
    print(f'''Time of execution of python implementation
 is {end_ts-start_ts} seconds''')
    print("==== ctypes ====")
    start_ts = time.time()
    res_c = [mult.c_matmult(x, y) for x, y in zip(a_arg, b_arg)]
    end_ts = time.time()
    print(f'''Time of execution of ctypes implementation
 is {end_ts-start_ts} seconds''')
    res_numpy = [numpy.matmul(x, y).tolist() for x, y in zip(a_arg, b_arg)]
    assert res_py == res_c == res_numpy


if __name__ == "__main__":
    main()
