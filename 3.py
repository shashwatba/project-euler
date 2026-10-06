import math

def main():
    total = 600851475143
    array_of_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    prime_checker = 59*59


    while prime_checker > 59:
        is_prime = True
        for i in range(0, len(array_of_primes)):
            if prime_checker % array_of_primes[i] == 0:
                is_prime = False
                break
        if is_prime:
            array_of_primes.append(prime_checker)
        prime_checker -= 1

    new_array_of_primes = sorted(array_of_primes)

    print(math.sqrt(math.sqrt(600851475143)))

    prime_checker = 0
    for a in new_array_of_primes:
        if a < 881:
            prime_checker = a

    print(prime_checker)
    print(len(new_array_of_primes))



    final_array = []
    prime_checker = prime_checker**2
    while prime_checker > 1:
        is_prime = True
        for i in range(0, len(new_array_of_primes)):
            if prime_checker % new_array_of_primes[i] == 0:
                is_prime = False
                break
        if is_prime:
            #print("hi")
            final_array.append(prime_checker)
        prime_checker -= 1
        

        
    for num in final_array:
        if total % num == 0:
            print(num)
            return -1




    

if __name__ == "__main__":
    main()