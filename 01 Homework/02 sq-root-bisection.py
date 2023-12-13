'''
This program will modify your previous square root algorithm 
by using a bisection search in Chap 3 of your textbook. 
'''
def square_root(x, root, epsilon):
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**root - x) >= epsilon:
        if ans**root < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

x = float(input("Enter a number: "))
epsilon = 0.00001
print("The square root of", x, "is approximately", square_root(x, 2, epsilon))