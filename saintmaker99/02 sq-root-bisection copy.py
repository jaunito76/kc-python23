'''
This program will modify your previous square root algorithm 
by using a bisection search in Chap 3 of your textbook. 
'''
def sqr(f):
    epsilon=0.01
    k=float(input('Enter a float or int for a square root please:'))
    guess=k/2
    while abs(guess**2-k)>=epsilon:
        guess=guess-(((guess**2)-k)/(2*guess))
    print('square root of', k, 'is about', guess)
    return guess
print(sqr(1))
f=float(input('Enter a float or int for a square root please:'))
sqr(f)
