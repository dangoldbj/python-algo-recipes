from concurrent.futures import ThreadPoolExecutor
import time
def f():
    print("INSIDE F")
    time.sleep(10)
    return 1

def g():
    print("Inside G")
    time.sleep(5)
    print("Returning from g")
    return 2


def main():
    with ThreadPoolExecutor() as pool:
        t1 = pool.submit(f)
        t2 = pool.submit(g)
        print(max(t1.result(), t2.result()))

if __name__ == '__main__':
    main()