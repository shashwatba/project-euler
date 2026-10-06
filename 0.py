def main():
    sum = 0
    for i in range(1,384001):
        if i % 2 != 0:
            sum += (i*i)


    print(sum)


if __name__ == "__main__":
    main()