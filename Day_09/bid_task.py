import os

bids = {}
addusers = True
choise = 'yes'
i = 1

if __name__ == '__main__':

    while addusers:
        name = input('What is your name?:')
        bid = input('What''s your bid?:')
        # bids['user_{}'.format(i)] = name
        # bids['bid_{}'.format(i)] = bid
        bids[f'{name}'] = int(bid)
        choice = input('Do you want make a bid? \n please enter yes or no: \n')
        # i += i
        if choice == 'yes':
            addusers = True
        else:
            addusers = False
    # Set the TERM environment variable to xterm to avoid issues with clearing the screen
    os.environ['TERM'] = 'xterm'
    # Clear screen on Mac (Unix-like system)
    
    print(bids)

    #  bids = {'Jon': 16, 'Brian': 45, 'Ivan': 12}

    max_bidder = max(bids, key=lambda k: bids[k])

    print(f"The maximum bid is {bids[max_bidder]} by {max_bidder}")

