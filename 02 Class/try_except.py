def main():
    x = get_int()
    print("x squared is ", x * x)


def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
            print("x is not an integer")


if __name__ == "__main__":
    main()
