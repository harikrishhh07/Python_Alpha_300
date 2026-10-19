
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

        suits = ["spades", "clubs", "hearts", "diamonds"]

        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number=1):
        cards_dealt = []

        for _ in range(min(number, len(self.cards))):
            cards_dealt.append(self.cards.pop())

        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        aces = 0

        for card in self.cards:
            self.value += card.rank["value"]

            if card.rank["rank"] == "A":
                aces += 1

        while self.value > 21 and aces > 0:
            self.value -= 10
            aces -= 1

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        name = "Dealer's" if self.dealer else "Your"
        print(f"{name} hand:")

        for index, card in enumerate(self.cards):
            if (
                index == 0
                and self.dealer
                and not show_all_dealer_cards
            ):
                print("Hidden card")
            else:
                print(card)

        if not self.dealer or show_all_dealer_cards:
            print("Value:", self.get_value())

        print()


class Game:
    def play(self):
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(
                    input("How many games do you want to play?: ")
                )

                if games_to_play <= 0:
                    print("Enter a positive number.")

            except ValueError:
                print("You must enter a valid whole number.")

        game_number = 0

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for _ in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""

            while choice not in ["s", "stand"] and player_hand.get_value() < 21:
                choice = input(
                    "Please choose Hit or Stand (H/S): "
                ).lower().strip()

                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input(
                        "Please enter Hit or Stand (H/S): "
                    ).lower().strip()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            dealer_hand.display(show_all_dealer_cards=True)

            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal())

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(
                player_hand, dealer_hand, game_over=True
            )

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()

        if not game_over:
            if player_value > 21:
                print("You busted. Dealer wins!")
                return True

            elif dealer_value > 21:
                print("Dealer busted. You win!")
                return True

            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both players have Blackjack! Tie!")
                return True

            elif player_hand.is_blackjack():
                print("You have Blackjack! You win!")
                return True

            elif dealer_hand.is_blackjack():
                print("Dealer has Blackjack! Dealer wins!")
                return True

            return False

        if player_value > dealer_value:
            print("You win!")
        elif player_value == dealer_value:
            print("Tie!")
        else:
            print("Dealer wins!")

        return True


game = Game()
game.play()
