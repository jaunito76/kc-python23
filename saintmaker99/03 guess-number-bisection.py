'''
This program will allow the user to come up with a number in his or her
head and then the computer will try to guess the number using a bisection
search. The user will enter higher ('h'), lower ('l'), or exact ('e').

The user will guess between 0 and 100 and the computer will only guess
whole numbers (no decimals). The computer will print out the guess on
each iteration, and then at the end it will print out:
'Your answer is: ' <the number found>
'The computer took <number of guesses to find your number'> guess(es)
'''
g = 50
gn = 0

c = 0
while c != 'e':
    c = input(f'The computor guesses {g}, \nHigher, lower or exactly (h,l,e): ')
    if c == 'h':
        g = int(g*1.5)
        gn = gn+1
    elif c == 'l':
        g = int(g/2)
        gn = gn+1
    elif c == 'e':
        print('Your answer is: ', g, 'The computer took', gn, 'guess(es)')