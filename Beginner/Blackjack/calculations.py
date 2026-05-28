import random

def deal_your_cards(cards_storage):
    your_cards = []
    your_cards.append(cards_storage[random.randint(0, len(cards_storage) - 1)])
    your_cards.append(cards_storage[random.randint(0, len(cards_storage) - 1)])

    return your_cards

def deal_computer_cards(cards_storage):
    computer_cards = []
    computer_cards.append(cards_storage[random.randint(0, len(cards_storage) - 1)])
    return computer_cards


def get_cards(given_card_set, cards_storage):
    given_card_set.append(cards_storage[random.randint(0, len(cards_storage) - 1)])

    return given_card_set


def score_while_playing (your_cards, computers_cards):
    your_current_score = sum(your_cards)
    print("Your cards:", your_cards, ", current score:", your_current_score)
    print("Computer's first card:", computers_cards[0])


def final_score (your_cards, computers_cards):
    your_final_score = sum(your_cards)
    computer_final_score = sum(computers_cards)
    print("Your final hand:", your_cards, ", final score:", your_final_score)
    print("Computer's final hand:", computers_cards, ", final score:", computer_final_score)


def computer_hand_calculations (computers_cards, cards_storage):
    while sum(computers_cards) < 17:
        get_cards(computers_cards, cards_storage)
    return computers_cards

def compare(your_cards, computers_cards):
    u_cards = sum(your_cards)
    c_cards = sum(computers_cards)

    if u_cards == c_cards:
        return "Draw 🙃"
    elif u_cards > 21:
        return "You went over. You lose 😭"
    elif u_cards == 21:
        return "You win 😃"
    elif c_cards > 21:
        return "Opponent went over. You win 😁"
    elif u_cards > c_cards:
        return "You win 😃"
    elif u_cards < c_cards:
        return "You lose 😤"
