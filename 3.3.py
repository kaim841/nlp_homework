def euclid(a, b):
    r = a % b
    while r:
        a, b = b, r
        r = a % b
    return b

def memory_move(n, k, a):
    q = euclid(n, k)
    for i in range(q):
        tmp = a[i]
        p = i
        for j in range(n // q):
            p = (p + k) % n
            s = a[p]
            a[p] = tmp
            tmp = s

def memory_moveP(n, k, a):
    q = euclid(n, k)
    for i in range(q):
        j = n // q - 1
        p1 = (i + j * k) % n
        tmp = a[p1]
        for j in range(j - 1, -1, -1):
            p2 = (i + j * k) % n
            a[p1] = a[p2]
            p1 = p2
        a[p2] = tmp

def main():
    a = [1, 2, 3, 4, 5, 6]
    k = 3
    memory_moveP(len(a), k, a)
    for item in a:
        print(item, end="\t")

if __name__ == "__main__":
    main()