import random

from WAR.Deck.cards import card_suit, card_rank, CARD


class DECK:

    def __init__(self):
        self.cards = []
        pass

    def initialise(self):
        for suit in card_suit:
            for rank in card_rank:
                self.cards.append(CARD(suit, rank))
        i = 0
        for suit in card_suit:
            for rank in card_rank:
                print(self.cards[i])
                i = i + 1
        print("Count is :%d", i)

    def shuffle(self):
        random.shuffle(self.cards)
        print("\n\n\nAfter Shuffle")
        i = 0
        for suit in card_suit:
            for rank in card_rank:
                print(self.cards[i])
                i = i + 1
