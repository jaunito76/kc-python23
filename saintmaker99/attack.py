import random
f1=0
num=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suits = [' of spades', ' of hearts', ' of clubs', ' of diamonds']
def extract_card_value(card_string):
    # Split the card string by space
    card_parts = card_string.split()

    # Extract the first part (which should be the card value)
    card_value = card_parts[0]

    # Convert the card value to an integer
    try:
        card_value = int(card_value)
    except ValueError:
        # If the conversion fails (e.g., for face cards), set card_value to None
        card_value = None

    return card_value

# Your existing code...
wins = 0
win = 0
c1 = ''
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
c1 = random.choice(num)
c1 = str(extract_card_value(c1))
cc1=c1
c1 += random.choice(suits)
if c1=='1':
    c1=c1+'/ace '
if c1=='11':
    c1=c1+'/jack'
if c1=='12':
    c1=c1+'/queen'
if c1=='13':
    c1=c1+'/king'

c2 = random.choice(num)
c2 = str(extract_card_value(c2))  # Convert to numeric value
cc2=c2
c2 += random.choice(suits)
if c2=='1':
    c2=c2+'/ace'
if c2=='11':
    c2=c2+'/jack'
if c2=='12':
    c2=c2+'/queen'
if c2=='13':
    c2=c2+'/king'

c3 = random.choice(num)
c3 = str(extract_card_value(c3))  # Convert to numeric value
cc3=c3
c3 += random.choice(suits)
if c3=='1':
    c3=c3+'/ace'
if c3=='11':
    c3=c3+'/jack'
if c3=='12':
    c3=c3+'/queen'
if c3=='13':
    c3=c3+'/king'

print(f"You have a hand of: a(n) {c1}, a(n) {c2}, and a(n) {c3}. The enemy's hand is unknown.")


# Generate opponent's hand
v1 = random.choice(num)
v1 = str(extract_card_value(v1))  # Convert to numeric value
vv1=v1

if v1=='1':
    v1=v1+'/ace '
if v1=='11':
    v1=v1+'/jack'
if v1=='12':
    v1=v1+'/queen'
if v1=='13':
    v1=v1+'/king'
v1 += random.choice(suits)
v2 = random.choice(num)
v2 = str(extract_card_value(v2))  # Convert to numeric value
vv2=v2

if v2=='1':
    v2=v2+'/ace '
if v2=='11':
    v2=v2+'/jack'
if v2=='12':
    v2=v2+'/queen'
if v2=='13':
    v2=v2+'/king'
v2 += random.choice(suits)
v3 = random.choice(num)
v3 = str(extract_card_value(v3))  # Convert to numeric value
vv3=v3

if v3=='1':
    v3=v3+'/ace '
if v3=='11':
    v3=v3+'/jack'
if v3=='12':
    v3=v3+'/queen'
if v3=='13':
    v3=v3+'/king'
v3 += random.choice(suits)
r1=''
f1=0
while f1<3:
    r1=input(print( "enter a card; your choices are card1 card2 and card3                                    "))
    if r1=='card1':
        c1='Empty slot (previosly card 1)'
        f1+=1
        if vv1>cc1:
            wins+=1
            print("you lost that round, the enemy's face value was", vv1, 'and yours was', cc1)
        elif vv1==cc1:
            Print('oh dang, a tie')
        elif vv1<cc1:
            print("you won that round, the enemy's face value was", vv1, 'and yours was', cc1)
            win+=1
    if r1=='card2':
        c2='Empty slot (previosly card 2)'
        f1+=1
        if vv2>cc2:
            wins+=1
            print("you lost that round, the enemy's face value was", vv2, 'and yours was', cc2)
        elif vv2==cc2:
            Print('oh dang, a tie')
        elif vv2<cc2:
            print("you won that round, the enemy's face value was", vv2, 'and yours was', cc2)
            win+=1
    if r1=='card3':
        c1='Empty slot (previosly card 1)'
        f1+=1
        if vv3>cc3:
            wins+=1
            print("you lost that round, the enemy's face value was", vv3, 'and yours was', cc3)
        elif vv3==cc3:
            Print('oh dang, a tie')
        elif vv3<cc3:
            print("you won that round, the enemy's face value was", vv3, 'and yours was', cc3)
            win+=1
if wins>win:
    print('oh well, it appears you lost. better luck next time')
elif wins==win:
    print("you tied, or met your match however you want to look at it. the only thing you need to remember is that I didn't lose to you. bet you feel pretty bad about failing to win against an uninteligent robot, but oh well, sucks to suck I guess")
else:
    print("you won, wow! want to try again?")