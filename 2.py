def main():
    sum = 0
    i = 1
    j = 2
    while j <= 4000000:
        if i % 2 == 0:
            sum += i
        if j % 2 == 0:
            sum += j
        i = j + i
        j = j + i

    print(sum)


if __name__ == "__main__":
    main()