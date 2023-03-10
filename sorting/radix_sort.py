from counting_sort import counting_sort
import math

def radix_sort(a):
    largest = max(a)
    d = len(str(largest))
    # base = math.ceil(math.log(largest, len(a)))
    base = 10
    out = []
    for i in range(d):
        out = counting_sort(a, key=lambda x: x % base**(i+1))
    return out


if __name__ == '__main__':
    l = [241,211,221,231,341,151, 31]
    print(radix_sort(l))