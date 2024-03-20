
import random
from typing import List, Optional

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.symbol = self.get_card_symbol()

    def get_card_symbol(self) -> str:
        suits_symbols = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        ranks_symbols = {
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': '10',
            'Jack': 'J',
            'Queen': 'Q',
            'King': 'K',
            'Ace': 'A'
        }
        return f"{ranks_symbols[self.rank]}{suits_symbols[self.suit]}"

    def __str__(self) -> str:
        return f"{self.symbol}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.is_empty():
            return self.cards.pop()
        else:
            print("Deck is empty. Cannot draw a card.")
            return None

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def return_cards(self, cards: List[Card]) -> None:
        self.cards.extend(cards)

    def __str__(self) -> str:
        deck_str = ", ".join(str(card) for card in self.cards)
        return f"Deck of Cards: {deck_str}"
    
class Hand:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: 'Card') -> None:
        self.cards.append(card)

    def display_hand(self) -> str:
        hand_str = ", ".join(str(card) for card in self.cards)
        return f"Hand: {hand_str}"

    def draw_card(self) -> Optional['Card']:
        """
        Draw a card from the hand.

        Returns:
            Card or None: The card drawn from the hand, or None if the hand is empty.
        """
        if self.cards:
            return self.cards.pop()
        else:
            print("Hand is empty. Cannot draw a card.")
            return None
    def is_empty(self) -> bool:
        """
        Check if the hand is empty.

        Returns:
            bool: True if the hand is empty, False otherwise.
        """
        return len(self.cards) == 0
def main():
    # Example usage:
    my_deck = Deck()
    my_deck.shuffle()

    # Draw and print 5 cards from the deck
    for _ in range(5):
        card = my_deck.draw_card()
        if card:
            print(card)

if __name__=="__main__":
    main()