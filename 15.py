def main():

    product_a = 1
    for i in range(1,41):
        product_a *= i

    product_b = 1
    for j in range (1,21):
        product_b *= j

    product_b = product_b ** 2

    return product_a / product_b

if __name__ == "__main__":
    print(main())