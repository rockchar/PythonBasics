"""
Defines the card class

"""
card_suit = ["HEARTS", "DIAMONDS", "SPADES", "CLUBS"]
card_rank = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE"]
card_value = {"TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9, "TEN": 10,
              "JACK": 11, "QUEEN": 12, "KING": 13, "ACE": 14}


class CARD:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_value[rank]

    def __str__(self):
        return "\n CARD object is {0} of {1}".format(self.rank,self.suit)

