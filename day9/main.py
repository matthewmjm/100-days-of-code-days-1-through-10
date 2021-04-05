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
        print(the_bids)
        # print(f"The winner is {first_name} with a bid of ${bid}!\n")