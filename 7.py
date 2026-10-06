def main():

    list_of_primes = [2,3,5,7,11,13,17,19,23]

    i = 25
    while len(list_of_primes) < 100001:
        is_prime = True
        upper_limit = int(i ** 0.5) + 1
        for num in range(2,upper_limit):
            if i % num == 0:
                is_prime = False
                break

        if is_prime:
            list_of_primes.append(i)
        is_prime = True
        i += 2

    return list_of_primes[100000]


if __name__ == "__main__":
    print(main())


