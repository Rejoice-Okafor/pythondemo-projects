#This is a project to demonstrate function creation, the while and for loops as well as usage of the logic operands(True/False)


logo_3 = """

  _____                 _                              
 / ___/_ _____ ___ ___ (_)__  ___ ____ ____ _  __ _  ___ 
/ (_ / // / -_|_-<(_-</ / _ \/ _ `/ _ `/ _ `/  ' \/ -_)
\___/\_,_/\__/___/___/_/_//_/\_, /\_, /\_,_/_/_/_/\__/ 
                            /___//___/                 
"""

print(logo_3)

bids = {}
is_bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not is_bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    print(bids)
    bid_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if bid_continue == 'no':
        highest_bidder(bids)
        is_bidding_finished = True
    
