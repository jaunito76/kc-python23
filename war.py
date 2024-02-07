# from deck import *
import deck as d

def main() -> None:
    # Example usage:
    my_deck = d.Deck()
    my_deck.shuffle()
    hands = []
    # deal to both hands
    # print(type(my_deck.cards.copy()))
    hands = deal(my_deck)
    # for hand in hands:
    #     print(hand)
    # play the game
    play_war(hands)


def deal(deck: d.Deck) -> list["d.Hand"]:
    hand1 = d.Hand()
    hand2 = d.Hand()
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


def play_war(hands: list[d.Hand]) -> str:
    while not (hands[0].is_empty() or hands[1].is_empty()):
        # play top card
        # 
            # who is the winner of the top card
                # if face value is the same
                    # play top three cards (hidden) and a fourth card (shown)
                    # who is the winner
                # else
                    # loser card goes to winner's hand
        pass

if __name__=='__main__':
    main()