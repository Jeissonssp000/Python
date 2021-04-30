import random
import collections

SUITS = ['espada', 'corazon', 'rombo', 'trebol']
VALUES = [i for i in range(1,14)]


def create_deck():
    decks = []
    for deck in SUITS:
        for value in VALUES:
            decks.append( ( deck, value ) ) 
    
    return decks


def get_hand(decks, hand_size):
    hand = random.sample(decks, hand_size)
    return hand


def is_straight(values):
    """Compare two list: 
    sorted input list vs new list created as a range with the min and max value"""
    return sorted(values) == list(range(min(values), max(values)+1)) 


def main(hand_size, attemps):

    #Variables...
    pair_flag = False
    trio_flag = False
    flush_flag = False
    straight_flag = False

    pairs = 0
    two_pairs = 0
    trio = 0
    straight = 0
    flush = 0
    full_house = 0
    straight_flush = 0
    poker = 0
    decks = create_deck()
    hands = []

    #Create hands...
    for _ in range(attemps):
        hand = get_hand(decks, hand_size)
        hands.append(hand)

    #Loop over the hands to find the probabilities
    for hand in hands:
        values = []
        suits = []

        for card in hand:
            values.append(card[1])
            suits.append(card[0])

        counter_values = dict(collections.Counter(values))
        counter_suits = dict(collections.Counter(suits))

        pair_flag = False
        trio_flag = False
        flush_flag = False
        straight_flag = False

        #PAIR, TWO PAIR, TRIPS and POKER
        for val in counter_values.values():
            if val == 2:
                if pair_flag:
                    two_pairs += 1
                else:
                    pairs += 1
                    pair_flag = True
            if val == 3:
                trio += 1
                trio_flag = True
            if val == 4:
                poker += 1

        #FLUSH
        for val in counter_suits.values():
            if val == hand_size:
                flush += 1
                flush_flag = True
                break
        
        #FULL HOUSE: We need a pair and a Three of a kind
        if pair_flag and trio_flag:
            full_house += 1

        #STRAIGHT: Consecutives values
        if is_straight(values):
            straight += 1
            straight_flag = True
        
        #STRAIGHT FLUSH: Straight + Flush
        if straight_flag and flush_flag:
            straight_flush += 1

    print(f'The PAIR probability for the hand size {hand_size} is {pairs / attemps}')
    print(f'The TWO PAIR probability for the hand size {hand_size} is {two_pairs / attemps}')
    print(f'The THREE OF A KIND probability for the hand size {hand_size} is {trio / attemps}')
    print(f'The STRAIGHT probability for the hand size {hand_size} is {straight / attemps}')
    print(f'The FLUSH probability for the hand size {hand_size} is {flush / attemps}')
    print(f'The FULL HOUSE probability for the hand size {hand_size} is {full_house / attemps}')
    print(f'The POKER probability for the hand size {hand_size} is {poker / attemps}')
    print(f'The STRAIGHT FLUSH probability for the hand size {hand_size} is {straight_flush / attemps}')
     

if __name__ == "__main__":

    hand_size = int(input('Size Hand: '))
    attemps = int(input('Attemps: '))

    main(hand_size, attemps)