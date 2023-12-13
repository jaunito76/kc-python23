def main():
    pyramid(int(input("How high would you like your pyramid? ")))
    
def pyramid(n):
    for i in range(n):
        s = '#' * (i + 1)
        print(s.rjust(n))

if __name__ == "__main__":
    main()