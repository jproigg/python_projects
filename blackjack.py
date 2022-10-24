from secrets import choice


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(list_cards):
    return sum(list_cards)


print("dealing to user")

user_cards = []

card_1 = deal()
card_2 = deal()

user_cards.append(card_1)
user_cards.append(card_2)

print(user_cards)


print("dealing to computer")

computer_cards = []

card_1 = deal()
card_2 = deal()

computer_cards.append(card_1)
computer_cards.append(card_2)

print(computer_cards)


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(user_score)
print(computer_score)
