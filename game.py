from deck import Deck
from player import Player,Dealer

class BlackjackGame:
    def __init__(self, player_name):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(player_name)
        self.dealer = Dealer()

    def start_game(self):
        # Deal 2 cards to player and dealer
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

        print(f"Dealer shows: {self.dealer.hand.cards[0]}")
        print(f"{self.player.name}'s hand: {[str(card) for card in self.player.hand.cards]} (Value: {self.player.hand.value})")

    def player_turn(self):
        while True:
            # Show current hand
            print(f"\n{self.player.name}'s hand: {[str(card) for card in self.player.hand.cards]} (Value: {self.player.hand.value})")
            
            # Check if busted
            if self.player.is_busted():
                print(f"{self.player.name} busted! Dealer wins.")
                return False

            # Ask player to Hit or Stand
            choice = input("Do you want to Hit or Stand? (h/s): ").lower()
            if choice == 'h':
                self.player.hit(self.deck)
            elif choice == 's':
                print(f"{self.player.name} stands with value {self.player.hand.value}")
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")
        return True

    def dealer_turn(self):
        print("\nDealer's turn:")
        print(f"Dealer's hand: {[str(card) for card in self.dealer.hand.cards]} (Value: {self.dealer.hand.value})")
        self.dealer.play_turn(self.deck)
        print(f"Dealer's final hand: {[str(card) for card in self.dealer.hand.cards]} (Value: {self.dealer.hand.value})")

    def check_winner(self):
        player_val = self.player.hand.value
        dealer_val = self.dealer.hand.value

        if self.player.is_busted():
            print("Dealer wins!")
        elif self.dealer.is_busted():
            print(f"{self.player.name} wins! Dealer busted.")
        else:
            if player_val > dealer_val:
                print(f"{self.player.name} wins!")
            elif dealer_val > player_val:
                print("Dealer wins!")
            else:
                print("It's a tie! Push.")

    def play(self):
        self.start_game()

        # Player turn
        if self.player_turn():
            # Dealer turn only if player did not bust
            self.dealer_turn()

        # Determine winner
        self.check_winner()
# main.py or at the bottom of your game file

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = BlackjackGame(player_name)  
    game.play()                         
