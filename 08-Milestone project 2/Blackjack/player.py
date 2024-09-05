

class Player():
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.hand = []
        self.value = 0
        self.aces = 0
    
    def __str__(self):
        return f'{self.name}, you have ${self.balance}'
    
    def place_bet(self):
        amount = -1.0
        print('Please place your bet!')
        while amount < 0 or amount > self.balance:
            try:
                amount = float(input('Place bet: '))
            except:
                print('Error occured, try again!')
            else:
                if amount < 0 or amount>self.balance:
                    print('The amount entered is not possible!')
        
        self.balance-=amount
        print('You have betted ', amount)
        return amount
    
    def add_balance(self,amount):
        self.balance+=amount
    
    def add_card(self,card):
        self.hand.append(card)
        if card.rank == 'Ace':
            self.aces+=1
        self.value += card.value
    
    def adjust_aces(self):
        while self.value < 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def reset(self):
        self.hand = []
        self.value = 0
        self.aces = 0