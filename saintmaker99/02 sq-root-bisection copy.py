'''
This program will modify your previous square root algorithm 
by using a bisection search in Chap 3 of your textbook. 
'''
def sqr(f):
    x=0
    while (x*x)<f:
        x=x + 0.001
        print(x)
print(sqr(1))
f=float(input('Enter a float or int for a square root please:'))
sqr(f)
