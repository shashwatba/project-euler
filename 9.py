def main():
    squares = []
    for i in range(1, 1000):
        squares.append(i)

    for i in range(1,1000):
        for j in range(i+1,1000):
            c = 1000 - i - j
            if (i**2) + (j**2) == c**2:
                return (i*j*c)






if __name__ == "__main__":
    print(main())