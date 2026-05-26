from art import logo

print(logo)



def find_highest_bid(bid_log):
    winner = ''
    highest_bid = 0

    for name in bid_log:
        if bid_log[name] > highest_bid:
            highest_bid = bid_log[name]
            winner = name
    print('The winner is' ,winner, 'with a bid of $',highest_bid)

bid_log = {}

cont = True
while cont:
    name = input('What is your name?:   ')
    bid = input('What is your bid?: $  ')
    bid_log[name] = int(bid)
    more_bidders = input("Are there any other bidder? Type 'yes' or 'no': ")
    if more_bidders == 'no':
        cont = False
    elif more_bidders == 'yes':
        print("\n" * 100)


find_highest_bid(bid_log)
