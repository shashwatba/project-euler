def main():
    x = 2**1000
    sum = 0
    while x >= 10:
        remainder = x % 10
        sum += remainder
        x = x // 10

    sum += x
    print(x)
    print(sum)


if __name__ == "__main__":
    print(main())