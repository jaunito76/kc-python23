# from deck import *
from cards import *


def main() -> None:
    # Example usage:
    my_deck = Deck()
    my_deck.shuffle()
    hands = deal(my_deck)
    print(hands[0])
    print(hands[1])
    play_war(hands)

def deal(deck: Deck) -> list["Hand"]:
    hand1 = Hand()
    hand2 = Hand()
    try:
        for _ in deck.cards.copy():
            hand1.get_cards([deck.draw_card()])
            hand2.get_cards([deck.draw_card()])
    except EOFError:
        pass
    except:
        print("There was an unanticipated Error, please review your code")
    finally:
        print("Hands have been dealt")
    return [hand1, hand2]


def play_war(hands: list[Hand]) -> str:
    while  (len(hands[0]) > 0 and len(hands[1]) > 0):
        card1 = hands[0].play_top_card()
        card2 = hands[1].play_top_card()
        cards_played=[card1, card2]
        #print(f'type of card 1 {type(card1)}')
        if card1 < card2:
            hands[1].get_cards(cards_played)
        elif card1 > card2:
            hands[0].get_cards(cards_played)
        else:
            winner = war(hands, cards_played)
            hands[winner].get_cards(cards_played)
        print(f'Card 1: {card1} Card 2: {card2}')
        #print(f'Hand 1: {hands[0].show_hidden_cards()}')
        #print(f'Hand 2: {hands[1].show_hidden_cards()}')
        print(f'Cards in Hand 1: {len(hands[0])} Cards in Hand 2: {len(hands[1])}')
        input("Enter")
    if len(hands[0] > 0):
        return 'Player 1 Wins!'
    else:
        return 'Player 2 Wins!'
    
def war(hands: list[Hand], cards_played: list[Card]) -> int:
    #returns the winner as 1 or 0
    for _ in range(4):
        try:
            cards_played.append(hands[0].play_top_card)
        except:
            return 1
        try:
            cards_played.append(hands[1].play_top_card)
        except:
            return 0
    player_1_card = cards_played[len(cards_played)-2]
    player_2_card = cards_played[len(cards_played)-1]
    print(type(player_2_card))
    return 0
    # if player_1_card == player_2_card:
    #     war(hands, cards_played)
    # elif player_1_card > player_2_card:
    #     return 0
    # else:
    #     return 1
        
            
if __name__=='__main__':
    main()