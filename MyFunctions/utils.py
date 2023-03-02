def time(func, *args):
    start = perf_counter()
    a = func(*args)
    print(perf_counter() - start)
    return a
