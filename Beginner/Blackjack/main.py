import art
import calculations
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    print(art.logo)

    #Get your cards
    your_cards = calculations.deal_your_cards(cards)

    #Show computers first card
    computers_cards = calculations.deal_computer_cards(cards)

    #Scoreboard
    calculations.score_while_playing(your_cards, computers_cards)


    if sum(your_cards) != 21:
        keep_hitting = True
        while keep_hitting:
            keep_going = input("Type 'y' to get another card or type 'n' to pass: ")
            if keep_going == 'y':
                your_cards = calculations.get_cards(your_cards, cards)
                if sum(your_cards) >= 21:
                    if 11 in your_cards:
                        your_cards[your_cards.index(11)] = 1
                        calculations.score_while_playing(your_cards, computers_cards)
                    else:
                        keep_hitting = False
                        calculations.score_while_playing(your_cards, computers_cards)
                        calculations.final_score(your_cards, computers_cards)
                else:
                    calculations.score_while_playing(your_cards, computers_cards)

            else:
                keep_hitting = False
                computers_cards = calculations.computer_hand_calculations(computers_cards, cards)
                calculations.final_score(your_cards, computers_cards)


    print(calculations.compare(your_cards, computers_cards))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
