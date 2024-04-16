# create card deck 
import random
    
values = [list(range(2,14))]
suits = ["clubs","diamonds","spades","hearts"]

face_cards = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"
    
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value 
        else:
            raise ValueError(f'Type of other card is {type(other)}')
    
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value 
        else:
            raise ValueError(f'Type of other card is {type(other)}')
    
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        else:
            return False
    
    def same_suit(self, card):
        return card.suit == self.suit
    
    def same_value(self, card):
        return card.value == self.value
    
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "K", "A"]
        
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __str__(self) -> str:
        deck_str = '\n'.join(str(card) for card in self.cards)
        return f"deck of cards: {deck_str}"
    
        
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def return_cards(self, cards: list[Card]) -> None:
        self.cards.extend(cards)

def main():
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)

class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.showing_cards = []
        self.hidden_cards = []
        
    def discard(self, card: Card) -> Card:
        self.cards.remove(card)
        return card

    def play(self, cards: list[Card]) -> None:
        self.hidden_cards.remove(cards)
        self.showing_cards.extend(cards)

    def get_cards(self, cards: list[Card]) -> None:
        self.return_cards(cards)
        #print(f'Self.cards {", ".join([str(card) for card in self.cards])}')
        self.hidden_cards.extend(cards)
        #print(f'Self.hidden_cards {", ".join([str(card) for card in self.hidden_cards])}')
    def played_cards(self) -> str:
        return 'Played Cards: ' + ','.join([str(card) for card in self.showing_cards])
    
    def __str__(self) -> str:
        return ("Played: " + ', '.join([card for card in self.showing_cards]) +
            '\nHand: ' + ', '.join([str(card) for card in self.hidden_cards]))
    def show_hidden_cards(self) -> str:
        display = ','.join([str(card) for card in self.hidden_cards])
        return "Still in Hand: " + display
    
    def play_top_card(self) -> Card:
        if len(self.hidden_cards) > 0:
            card = self.hidden_cards[0]
            self.cards.remove(card)
            self.hidden_cards.remove(card)
            return card
        else:
            raise Exception('Tried to play from an empty hand')
    
    def __len__(self) -> int:
        return len(self.hidden_cards)
            
def main() -> None:
    # Example usage:
    my_deck = Deck()
    my_deck.shuffle()
    hand = Hand()
    
    for _ in range(5):
        card = my_deck.draw_card()
        hand.get_cards([card])
    
    print(hand)
    
    

if __name__ == "__main__":
    main()