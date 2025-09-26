class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=card.value
        if card.rank=="A":
            self.aces+=1
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1