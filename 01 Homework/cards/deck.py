import random

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.symbol = self.get_card_symbol()

    def get_card_symbol(self) -> str:
        suits_symbols = {
            'hearts': '♥',
            'diamonds': '♦',
            'clubs': '♣',
            'spades': '♠'
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

    def same_suit(self, card) -> bool:
        return card.suit == self.suit
    
    def same_face(self, card) -> bool:
        return card.rank == self.rank

    def __str__(self) -> str:
        return f"{self.symbol:>3}"
    
    def __gt__(self, other: 'Card') -> bool:
        return self.rank > other.rank
    
    def __eq__(self, other: 'Card') -> bool:
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other: 'Card') -> bool:
        return self.rank < other.rank
    
    def __ge__(self, other: 'Card') -> bool:
        return self.rank >= other.rank
    
    def __le__(self, other: 'Card') -> bool:
        return self.rank <= other.rank
    
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.is_empty():
            return self.cards.pop()
        else:
            raise EOFError('No cards remaining in the deck')    

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def return_cards_to_deck(self, cards: list[Card]) -> None:
        self.cards.extend(cards)

    def __str__(self) -> str:
        deck_str = ", ".join(str(card) for card in self.cards)
        return f"Deck of Cards: {deck_str}"
    
    def __iter__(self):
        return 

class Hand(Deck):
    def __init__(self):
        super.__init__(super())
        self.cards = []
        self.showing_cards = []
        self.hidden_cards = []

    def discard(self, card: Card) -> Card:
        self.cards.remove(card)
        return card

    def play_top(self) -> Card:
        if len(self.hidden_cards) == 0:
            raise ValueError('All cards have been played')
        
        my_card = self.hidden_cards.pop()
        try:
            self.cards.remove(my_card)
        except ValueError:
            pass
        try:
            self.showing_cards.remove(my_card)
        except ValueError:
            pass
        return my_card

    def play(self, cards: list[Card], stays_in_hand: bool = False) -> None:
        self.hidden_cards.remove(cards)
        if stays_in_hand:
            self.showing_cards.extend(cards)

    def take_a_trick(self, cards: list[Card]) -> None:
        try:
            self.hidden_cards.remove(cards)
        except:
            pass
        self.showing_cards.extend(cards)

    def recycle_cards(self) -> None:
        self.hidden_cards.extend(self.showing_cards)
        self.showing_cards = []

    def get_cards(self, cards: list[Card]) -> None:
        self.return_cards_to_deck(cards)
        self.hidden_cards.extend(cards)

    def played_cards(self) -> str:
        return 'Played Cards: ' + ','.join([str(card) for card in self.showing_cards])

    def show_hidden_cards(self) -> str:
        display = ','.join([str(card) for card in self.hidden_cards])
        return "Still in Hand: " + display
    
    def __str__(self) -> str:
        return self.show_hidden_cards() + ' ' + self.played_cards()

def main():
    pass

    # print(hand)
if __name__=="__main__":
    main()
