def output(a, length):
    # 输出结果，每6位一组，不足6位的前面补零
    print(a[length], end='')
    for i in range(length - 1, 0, -1):
        if a[i] >= 100000:
            print(a[i], end='')
        elif a[i] >= 10000:
            print(f"0{a[i]}", end='')
        elif a[i] >= 1000:
            print(f"00{a[i]}", end='')
        elif a[i] >= 100:
            print(f"000{a[i]}", end='')
        elif a[i] >= 10:
            print(f"0000{a[i]}", end='')
        else:
            print("000000", end='')

def big_digital(n):
    # 初始化数组，用于存储大数的每一位
    a = [0] * 30
    a[1] = 1
    length = 1  # 当前大数的长度
    for i in range(2, n + 1):
        d = 0  # 进位
        for j in range(1, length + 1):
            b = a[j] * i + d
            a[j] = b % 1000000
            d = b // 1000000
        if d != 0:
            a[length + 1] = d
            length += 1
    output(a, length)

# 测试代码
if __name__ == "__main__":
    big_digital(100)