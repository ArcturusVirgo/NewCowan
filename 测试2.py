from concurrent.futures import ProcessPoolExecutor

def ffunc():
    def fun(i):
        print(i)
        res = 1
        for j in range(1, 10000000):
            res += j

    pool = ProcessPoolExecutor()
    for i in range(10):
        pool.submit(fun, i)
    pool.shutdown()

if __name__ == '__main__':
    ffunc()
