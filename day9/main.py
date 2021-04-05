def add_bid(bidder_name, bidder_bid):
    new_bid = {}
    new_bid["first_name"] = bidder_name
    new_bid["bid"] = int(bidder_bid)
    the_bids.append(new_bid)

from art import logo
print(logo)
print("Welcome to the secret auction program.")
the_bids = []

other_bidders = False
while not other_bidders:
    first_name = input("What is your name?: ")
    bid = input("What's your bid?: $")

    add_bid(bidder_name=first_name, bidder_bid=bid)

    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if others == "no":
        other_bidders = True
        winning_bid = 0
        for bidder in the_bids:
            if bidder["bid"] > winning_bid:
                winning_bid = bidder["bid"]
                winner = bidder["first_name"]
        print(f"The winner is {winner} with a bid of ${winning_bid}!\n")