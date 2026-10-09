def main():
    counts = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    tens = [6,6,5,5,5,7,6,6]
    hundreds = [13,13,15,14,14,13,15,15,14]

    sum = 0
    for i in range(0, len(counts)):
        sum += counts[i]

    for j in range(0, len(tens)):
        sum += tens[j]
        for k in range(0, 9):
            sum += (tens[j] + counts[k])

    total = sum
    for num in hundreds:
        total += (num-3)
        total += ((num*99) + sum)

    return total + 11


if __name__ == "__main__":
    print(main())