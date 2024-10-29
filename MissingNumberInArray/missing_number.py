def find_missing_number(n, array):
    number_set = [0] * (n+1)
    for number in array:
        number_set[number - 1] = 1

    return number_set.index(0) + 1

def main():
    try:
        n = int(input("Input n: "))
        array = []
        print("Input {} numbers".format(n))
        for _ in range(n):
            array.append(int(input()))

        print("Missing number: ", find_missing_number(n, array))
    
    except TypeError:
        print("Invalid input type")

if __name__ == '__main__':
    main()