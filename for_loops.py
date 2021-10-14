from string import ascii_lowercase

if __name__ == '__main__':
    for i in range(10, 5, -1):
        print(i)
    print("\n")

    for i in range(0, 12, 3):
        print(i)
    print("\n")

    for i in range(5, 10):
        print(i)
    print("\n")

    for i in range(1, 10):
        if i == 5:
            print("Buzz")
        print("bizz")

    print("\n")

    for i in range(1,10):
        if i == 6:
            print("Found")
            break
        print("Not Yet")
    print("It was found at {}".format(i))
    print("\n")

    for ch in ascii_lowercase:
        print(ch)
    print("\n")