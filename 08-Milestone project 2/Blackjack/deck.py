from card import *
import random
'''
Deck class
'''

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.all_cards.append(new_card)
    
    def __len__(self):
        return len(self.all_cards)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        card = self.all_cards.pop()
        card.show_card()
        return card