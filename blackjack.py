from secrets import choice


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(list_cards):
 
    if sum(list_cards) == 21 and len(list_cards) == 2:
        return 0
    if 11 in list_cards and sum(list_cards) > 21:
        list_cards.remove(11)
        list_cards.append(1)
    return sum(list_cards)   

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'draw'
    elif computer_score == 0:
        return 'You lose, oponent has blackjack'
    elif computer_score > 21:
        return 'you win'
    elif user_score == 0:
        return "Black Jack, you win"
    elif user_score > 21:
        return "you lose"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
    

user_cards = []
computer_cards = []
is_game_over = False

for card in range(2):
    user_cards.append(deal())
    computer_cards.append(deal())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    status_user = print(f"your cards: {user_cards}, score: {user_score}")
    status_computer = print(f"computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal = input("type 'y' for another card, type 'n' to pass: ")
        if user_deal == "y":
            user_cards.append(deal())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal())
    computer_score = calculate_score(computer_cards)

print(f"your final score is {user_score}, this is your hand {user_cards}")
print(f"computer's final score is {computer_score}, this is your hand {computer_cards}")
print(compare(user_score, computer_score))
