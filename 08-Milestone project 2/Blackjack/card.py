'''
Card class
'''

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen',
         'King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9
              ,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False
        self.value = values[rank]
    
    def __str__(self):
        if self.face_up:      
            return f'{self.rank} of {self.suit}'
        else:
            return 'HIDDEN'
    
    def show_card(self):
        self.face_up = True

    def hide_card(self):
        self.face_up = False
