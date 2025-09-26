from hand import Hand
class Player:
    def __init__(self,name,chips=100):
        self.name=name
        self.hand=Hand()
        self.chips=chips
    
    def hit(self,deck):
        card=deck.deal_card()
        if card:
            self.hand.add_card(card)
    
    def is_busted(self):
        return self.hand.value>21

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
    
    def play_turn(self,deck):
        while self.hand.value<17:
            self.hit(deck)

