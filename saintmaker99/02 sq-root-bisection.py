'''
This program will modify your previous square root algorithm 
by using a bisection search in Chap 3 of your textbook. 
'''
num_geussses=0
x=0
epsilon=0.01
low=0
high=max(1, x)
ans=(high+low)/2
f=float(input('Enter a float or int for a suare root please:'))
high=f
while abs(ans**2-x)>=epsilon:
    print('low=', low, 'high=', high, 'ans=', ans)
    num_geussses+=1
    if ans**2<x:
        low=ans

    else:
        high=ans
    ans=(high+low)/2
print(num_geussses)
print(ans)