from typing import Type, List

from WAR.Players import player
from WAR.Deck import cards, deck
from WAR.Players.player import PLAYER


class GAME:

    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = deck.DECK()
        self.players: List[player.PLAYER] = []
        self.buffer: List[deck.CARD] = []

    def deal_cards(self):
        cards_per_player = int(52 / self.num_players)
        print(f"Cards per player is {cards_per_player}")
        self.deck.initialise()
        self.deck.shuffle()
        self.create_players()
        for i in range(0, cards_per_player):
            for j in range(0, self.num_players):
                self.players[j].add_card(self.deck.cards[i * self.num_players + j])
        self.play()

    def begin_game(self):
        print(f"Playing {self.num_players} players\n")
        self.deal_cards()

    def create_players(self):
        for i in range(0, self.num_players):
            self.players.append(player.PLAYER(i))

    def check_winner(self):
        pass

    def play(self):
        while True:
            if self.players[0].cards[-1].value > self.players[1].cards[-1].value:
                self.players[0].add_card(self.players[1].cards.pop(-1))
                if len(self.buffer)>0:
                    self.players[0].add_card(self.buffer)
                print(f"player 0 takes {self.players[0].cards[0]}")
                self.buffer.clear()
            elif self.players[0].cards[-1].value == self.players[1].cards[-1].value:
                print(f"WAR {self.players[0].cards[-1]} AND {self.players[1].cards[-1]}")
                self.buffer.append(self.players[1].cards.pop(-1))
                self.buffer.append(self.players[0].cards.pop(-1))
            elif self.players[0].cards[-1].value < self.players[1].cards[-1].value:
                self.players[1].add_card(self.players[0].cards.pop(-1))
                if len(self.buffer) > 0:
                    self.players[1].add_card(self.buffer)
                print(f"player 1 takes {self.players[1].cards[0]}")
                self.buffer.clear()

            if len(self.players[0].cards) == 0:
                print("Player 1 Wins")
                break
            elif len(self.players[1].cards) == 0:
                print("Player 0 Wins")
                break


g = GAME(2)
g.begin_game()
