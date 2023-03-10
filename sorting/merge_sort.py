from mydata import l
def merge_sort(A, s, e):
    if s == e:
        return [A[s]]
    m = (s + e) // 2
    l = merge_sort(A, s, m)
    r = merge_sort(A, m + 1, e)
    o = merge(l, r)
    return o

def merge(l, r):
    ls = 0
    rs = 0

    out = []
    while True:
        if ls == len(l):
            out.extend(r[rs:])
            break

        if rs == len(r):
            out.extend(l[ls:])
            break

        if l[ls] <= r[rs]:
            out.append(l[ls])
            ls += 1
        else:
            out.append(r[rs])
            rs += 1

    return out

print(merge_sort(l, 0, len(l) - 1))