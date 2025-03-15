def desert(distance):
    dis = 500
    oil = 500
    n = 1
    while dis < distance:
        print(f"station:{n}; distance:{dis}; oil:{oil}")
        n += 1
        oil += 500
        dis += 500 / (2 * n - 1)
    dis = distance - (dis - 500 / (2 * n - 1))
    oil = oil - 500 + dis * (2 * n - 1)

if __name__ == "__main__":
    desert(1000)