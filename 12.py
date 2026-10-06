def main():
    triangle_numbers = [1]
    for i in range(2, 1000000):
        triangle_numbers.append(i + triangle_numbers[-1])

    for num in triangle_numbers:
        divisors = 0
        for i in range(1,int((num+1)**.5)):
            if num == 1:
                break
            if num % i == 0:
                divisors += 2
            if divisors == 500:
                return num


    pass

if __name__ == "__main__":
    print(main())