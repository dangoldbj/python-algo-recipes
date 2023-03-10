
# for i in range(len(pos)):
#     t = pos[i]
#     pos[i] = s
#     s += t

# s = len(pos) - 1
# for i in range(len(pos) -1 , -1, -1):
#     pos[i] = s - pos[i]
#     s = pos[i]
# print(pos)

#TODO: negative values
#TODO: Hashing

def counting_sort(a, key=lambda x: x):
    k = max(map(key, a)) + 1
    pos = [0] * k
    for el in a:
        pos[key(el)] += 1

    s = 0
    for i in range(k):
        pos[i], s = s, s + pos[i]
    
    out = [0] * len(a)
    for i in range(len(a)):
        out[pos[key(a[i])]] = a[i]
        pos[key(a[i])] += 1
    return out

if __name__ == '__main__':
    l = [4,1,2,3,4,5, 3]
    print(counting_sort(l))