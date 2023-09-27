'''
This program will modify your previous square root algorithm 
by using a bisection search in Chap 3 of your textbook. 
'''
num_geussses=0
epsilon=0.00001
low=0
f=float(input('Enter a float or int for a square root please:'))
high=max(1, f)
ans=(high+low)/2
while abs(ans**2-f)>=epsilon:
    print('low=', low, 'high=', high, 'ans=', ans)
    num_geussses+=1
    if ans**2<f:
        low=ans
    else:
        high=ans
    ans=(high+low)/2
print('number of guesses',num_geussses)
print(num_geussses)
print('answer',ans)
print(ans)