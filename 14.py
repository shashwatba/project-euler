def main():
    collatz_sequence = 0
    tracker = {}
    max_value = 0
    number = 0
    
    for i in range(1, 1000000):
        num = i
        while num != 1:
            if num in tracker:
                collatz_sequence += tracker[num]
                break


            if num % 2 == 0:
                num = num//2
                collatz_sequence += 1
            else:
                num = (3*num) + 1
                collatz_sequence += 1


        tracker[i] = collatz_sequence
        max_value = max(collatz_sequence, max_value)
        if collatz_sequence == max_value:
            number = i
        collatz_sequence = 0

    return number
        

if __name__ == "__main__":
    print(main())

