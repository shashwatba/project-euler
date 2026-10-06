def main():
    list_of_multiples = [20,19,18,17,16,15,14,13,12,11]

    starting_point = 2520
    multiple = True
    while True:
        multiple = True
        for num in list_of_multiples:
            if starting_point % num != 0:
                multiple = False
                break
            if num == 11 and multiple == True:
                return starting_point
        starting_point += 20




    

if __name__ == "__main__":
    print(main())