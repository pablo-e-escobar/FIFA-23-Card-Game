import random
import pandas as pd
deck = 10

class Player():

    def __init__(self):
        self.name = "default"
        self.points = 0
        self.cards = list(range(1, deck+1, 1))

        random.shuffle(self.cards)

    def pick_card(self):
        picked_card = self.cards[0]
        self.cards.remove(picked_card)
        print(f"{self.name} drew {picked_card}")
        return picked_card

    def add_points(self):
        self.points += 1
        print(f"{self.name} wins the round")

    def game_over(self):
        return len(self.cards) == 0


p1 = Player()
p2 = Player()
p1.name = input("Enter Player1 name")
p2.name = input("Enter Player2 name")
print("Game Begins")

while True:
    input("Press Enter to pick cards")
    p1_card = p1.pick_card()
    p2_card = p2.pick_card()

    if p1_card > p2_card:
        p1.add_points()
    elif p2_card > p1_card:
        p2.add_points()
    else:
        print("Tie")

    data = {
      f"{p1.name}": [p1.points],
      f"{p2.name}": [p2.points]
    }

    sb = pd.DataFrame(data)

    print(sb.to_string(index=False))

    if p1.game_over() or p2.game_over():
        if p1.points > p2.points:
            print(f"{p1.name} wins!")
        elif p2.points > p1.points:
            print(f"{p2.name} wins!")
        else:
            print("Game ended as draw")
        print("Final Score")
        print(sb.to_string(index=False))
        break





