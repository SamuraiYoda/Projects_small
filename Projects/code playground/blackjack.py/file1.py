#comment#
#import random
# give user 2 random cards
# dictionary {  deck of cards } and {value of cards}
# add cards of user and of dealer
# inside while statement does the user or dealer have blackjack(=21)
#   if statement - user total =21 =  blackjack = win
#
#   elif dealer total =  21 = blackjack  user looses
# addition != 21 then
# user addition >21
#   if yes then does he have ace?
#       yes = use ace as 1
#           if total >21 user looses, if total < 21 game is still on
#       no = user looses                                           |
# ask if user wants another card - yes - total

import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
dealer_cards = []
is_game_over = False


def compare(user_score, dealer_score):
    if user_score > dealer_score:
        if user_score < 21:
            return ("you winn!")
        else:
            return ("you lose")
    elif dealer_score > user_score:
        if dealer_score < 21:
            return ("you lost")
        else:
            return ("You win as dealer score is greater than 21")
    elif dealer_score == user_score:
        return ("it's a draw")
    elif dealer_score == 0:
        return ("You loose opponent has blackjack")
    elif user_score == 0:
        return ("you win you have blackjack")
    else:
        return ("no specific condition's met")


#calculate sum of cards
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


#deal random cards to user
for _ in range(2):
    #  new_card = deal_cards()
    user_cards.append(deal_cards())
    dealer_cards.append(deal_cards())

#while loop for user
while not is_game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"user's cards are {user_cards}")
    print(f"dealer's cards are {dealer_cards[0]}")

    if user_score > 21 or user_score == 0 or dealer_score > 21 or dealer_score == 0:
        is_game_over = True
    else:
        user_should_deal = input("Do you wish to draw another card? Enter 'y' for yes and 'n' for no: ")
        if user_should_deal == 'y':
            user_cards.append(deal_cards())
            calculate_score()
        else:
            is_game_over = True


#while loop for dealer
while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_cards())
    dealer_score = calculate_score(dealer_cards)

print(f"your final hand is {user_score}, ")
print(f"Dealer's final score is {dealer_score}")

print(compare(user_score, dealer_score))
