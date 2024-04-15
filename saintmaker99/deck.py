import random
wins=0
win=0
c1=''
num=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
c1=random.choice(num)

if c1=='1':
    c1=c1+'/ace '
if c1=='11':
    c1=c1+'/jack'
if c1=='12':
    c1=c1+'/queen'
if c1=='13':
    c1=c1+'/king'
suits = [' of spades', ' of hearts', ' of clubs', ' of diamonds']
c1=c1 + random.choice(suits)
c2=''
c2=random.choice(num)
if c2=='1':
    c2=c2+'/ace'
if c2=='11':
    c2=c2+'/jack'
if c2=='12':
    c2=c2+'/queen'
if c2=='13':
    c2=c2+'/king'
c2=c2 + random.choice(suits)
c3=''
c3=random.choice(num)
if c3=='1':
    c3=c3+'/ace'
if c3=='11':
    c3=c3+'/jack'
if c3=='12':
    c3=c3+'/queen'
if c3=='13':
    c3=c3+'/king'
c3=c3 + random.choice(suits)
print('you have a hand of: ', 'a(n)', (c1+','), 'a(n)', (c2+','), 'and a(n) ', (c3+'.'),   "the enemy's hand is unknown")



v1=''
v1=random.choice(num)

if v1=='1':
    v1=v1+'/ace '
if v1=='11':
    v1=v1+'/jack'
if v1=='12':
    v1=v1+'/queen'
if v1=='13':
    v1=v1+'/king'
suits = [' of spades', ' of hearts', ' of clubs', ' of diamonds']
v1=v1 + random.choice(suits)

v2=''
v2=random.choice(num)

if v2=='1':
    v2=v2+'/ace '
if v2=='11':
    v2=v2+'/jack'
if v2=='12':
    v2=v2+'/queen'
if v2=='13':
    v2=v2+'/king'
suits = [' of spades', ' of hearts', ' of clubs', ' of diamonds']
v2=v2 + random.choice(suits)


v3=''
v3=random.choice(num)

if v3=='1':
    v3=v3+'/ace '
if v3=='11':
    v3=v3+'/jack'
if v3=='12':
    v3=v3+'/queen'
if v3=='13':
    v3=v3+'/king'
suits = [' of spades', ' of hearts', ' of clubs', ' of diamonds']
v3=v3 + random.choice(suits)
