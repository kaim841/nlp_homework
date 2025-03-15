def yanghui(a, n):
    a[0][0] = a[1][0] = a[1][1] = 1
    for i in range(2, n):
        a[i][0] = a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

def output(a, n):
    for i in range(n):
        for j in range(i + 1):
            print(a[i][j], end="\t")
        print()

if __name__ == "__main__":
    a = [[0 for _ in range(5)] for _ in range(5)]  # 创建一个5x5的二维列表并初始化为0
    yanghui(a, 5)
    output(a, 5)