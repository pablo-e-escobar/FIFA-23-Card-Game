import pandas as pd
import random

data = pd.read_csv('fifa23data.csv', usecols=['Full Name', 'Overall'])
df = pd.DataFrame(data)
df['Full Name'] = df['Full Name'].str.upper()

class Player:
    def __init__(self):
        self.name = "no_name_set"
        self.points = 0
        self.cards = df.sample(n=10).set_index(pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def pick_card(self):
        picked_card = self.cards.loc[0]
        print(f"{self.name} picks {picked_card['Full Name']}")
        self.cards = self.cards.drop([0])
        self.cards.reset_index(drop=True, inplace=True)
        return picked_card

    def add_points(self):
        self.points += 1

    def game_over(self):
        return len(self.cards) == 0


p1 = Player()
p2 = Player()
p1.name = input("Enter Team1 name")
p2.name = input("Enter Team2 name")
print("Game Begins")
while True:
    input("Press Enter to pick cards")
    p1_card = p1.pick_card()
    p2_card = p2.pick_card()

    if p1_card['Overall'] > p2_card['Overall']:
        p1.add_points()
        print(f"{p1_card['Full Name']} scores!!")
    elif p2_card['Overall'] > p1_card['Overall']:
        p2.add_points()
        print(f"{p2_card['Full Name']} scores!!")
    else:
        print("Both players fail to score")

    data = {
          f"{p1.name}": [p1.points],
          f"{p2.name}": [p2.points]
        }

    sb = pd.DataFrame(data)

    print(sb.to_string(index=False))

    if p1.game_over() or p2.game_over():
        if p1.points > p2.points:
            print(f"{p1.name} wins by {p1.points-p2.points} goals!!")
        elif p2.points > p1.points:
            print(f"{p2.name} wins by {p2.points-p1.points} goals!!")
        else:
            print("Game ended as draw!!")
        print("Final Score")
        print(sb.to_string(index=False))
        break