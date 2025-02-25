from typing import List

from WAR import Deck
from WAR.Deck import cards


class PLAYER:
    def __init__(self, player_num):
        self.cards: List[Deck.cards.CARD] = []
        self.player_num = player_num

    def add_card(self, card):
        if isinstance(card, list):
            self.cards.extend(card)
        else:
            self.cards.insert(0, card)

    def show_card(self):
        return self.cards.pop(-1)

    def __str__(self):
        return F"I am player number {self.player_num}"
