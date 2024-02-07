# from deck import *
from deck import Card, Deck, Hand
PLAYER1 = 0
PLAYER2 = 1
DISCARD = 2
WARCARDS = 3

def main() -> None:
    # Example usage:
    my_deck = Deck()
    my_deck.shuffle()
    hands = []
    # deal to both hands
    # print(type(my_deck.cards.copy()))
    hands = deal(my_deck)
    # for hand in hands:
    #     print(hand)
    # play the game
    play_war(hands)


def deal(deck: Deck) -> list['Hand']:
    hand1 = Hand()
    hand2 = Hand()
    hand3 = Hand()
    try:
        for _ in deck.cards.copy():
            hand1.get_cards([deck.draw_card()])
            hand2.get_cards([deck.draw_card()])
    except EOFError:
        pass
    except:
        print("There was an unanticipated Error, please reivew your code")
    finally:
        print("Hands have been dealt")
    return [hand1, hand2, hand3]


def play_war(hands: list['Hand']) -> str:
    secret_cards: list[Card] = []
    while not (hands[PLAYER1].is_empty() or hands[PLAYER2].is_empty()):
        # play top card
        card1, is_empty = play_to_empty(hands[PLAYER1])
        if is_empty:
            winner = PLAYER2
            break
        card2, is_empty = play_to_empty(hands[PLAYER2])
        if is_empty:
            winner = PLAYER1
            break
        
        print(f'Player 1 played {card1}')
        print(f'Player 2 played {card2}')
        print(f'Player 1: {hands[PLAYER1]}')
        print(f'Player 2: {hands[PLAYER2]}')
        if card1 > card2:
            print('Player 1 wins this round!')
            hands[PLAYER1].take_a_trick([card1,card2])
            if len(secret_cards) > 0:
                print('Player 1 wins the WAR!')
                hands[PLAYER1].take_a_trick(secret_cards)
                secret_cards = []
        elif card2 > card1:
            print('Player 2 wins this round!')
            hands[PLAYER2].take_a_trick([card1, card2])
            if len(secret_cards) > 0:
                print('Player 2 wins the WAR!')
                hands[PLAYER2].take_a_trick(secret_cards)
                secret_cards = []            
        else:
            print('Its a WAR!')
            for _ in range(WARCARDS):
                try:
                    secret_cards.append(hands[PLAYER1].play_top())
                except ValueError:
                    winner = PLAYER2
                    break
                try:
                    secret_cards.append(hands[PLAYER2].play_top())
                except ValueError:
                    winner = PLAYER1
                    break
            if len(secret_cards) < WARCARDS * 2:
                break
        input('Press Enter to continue')
            

def play_to_empty(hand: Hand) -> tuple(Card, bool):
    is_empty = False
    card = Card()
    try:
        card = hand.play_top()
    except ValueError:
        hand.recycle_cards()
        try:
            card = hand.play_top()
        except ValueError:
            is_empty = True
    return (card, is_empty)

if __name__=='__main__':
    main()