def isPalindrome(num):
    a = num % 10
    num_a = num // 10
    b = num_a % 10
    num_b = num_a // 10
    c = num_b % 10
    num_c = num_b // 10
    d = num_c % 10
    num_d = num_c // 10
    e = num_d % 10
    num_e = num_d // 10
    f = num_e % 10

    new_num = (a * 100000) + (b*10000) + (c*1000) + (d*100) + (e*10) + f
    return num == new_num



    

def main():
    max_palindrome = 100001
    first_number = 999
    
    while first_number > 900:
        second_number = 999
        while second_number > 900:
            product = first_number * second_number

            if isPalindrome(product) and product > max_palindrome:
                max_palindrome = product

            second_number -= 1

        first_number -= 1

    return max_palindrome


if __name__ == "__main__":
     print(main())