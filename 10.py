def main():
    list_of_primes = [2,3,5]
    divider = 3
    for i in range(7,2000000,2):
        is_prime = True
        while divider <= i**.5:
            if i % divider == 0:
                is_prime = False
                break
            divider += 2
        if is_prime:
            list_of_primes.append(i)
        is_prime = True
        divider = 3

    sum = 0
    for num in list_of_primes:
        sum += num

    return sum




if __name__ == "__main__":
    print(main())