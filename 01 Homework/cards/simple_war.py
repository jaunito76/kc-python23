from typing import List, Optional
from card_deck import Card, Deck, Hand

def compare_cards(card1: Card, card2: Card) -> int:
    """
    Compare two cards and return:
    -1 if card1 is lower
    0 if both cards are equal
    1 if card1 is higher
    """
    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    if rank_order.index(card1.rank) < rank_order.index(card2.rank):
        return -1
    elif rank_order.index(card1.rank) > rank_order.index(card2.rank):
        return 1
    else:
        return 0

def play_war() -> None:
    # Initialize the deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Deal the cards to two players
    player1_hand = Hand()
    player2_hand = Hand()

    while not deck.is_empty():
        player1_hand.add_card(deck.draw_card())
        player2_hand.add_card(deck.draw_card())

    # Play the game
    rounds = 0
    while True:
        rounds += 1
        print(f"\nRound {rounds}:")
        print("Player 1:", player1_hand.display_hand())
        print("Player 2:", player2_hand.display_hand())

        # Draw a card from each player's hand
        player1_card = player1_hand.draw_card()
        player2_card = player2_hand.draw_card()

        print("Player 1 plays:", player1_card)
        print("Player 2 plays:", player2_card)

        # Compare the cards
        comparison = compare_cards(player1_card, player2_card)
        if comparison == -1:
            print("Player 2 wins this round!")
            player2_hand.add_card(player1_card)
            player2_hand.add_card(player2_card)
        elif comparison == 1:
            print("Player 1 wins this round!")
            player1_hand.add_card(player1_card)
            player1_hand.add_card(player2_card)
        else:
            print("It's a tie!")

        # Check if any player has run out of cards
        if player1_hand.is_empty():
            print("\nPlayer 2 wins the game!")
            break
        elif player2_hand.is_empty():
            print("\nPlayer 1 wins the game!")
            break

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    play_war()
