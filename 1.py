def main():
    multiples = set()
    sum = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            if i not in multiples:
                multiples.add(i)
                sum += i



    print(sum)

if __name__ == "__main__":
    main()