from itertools import combinations as cb
from cards import rank_values

def deal_card(private_cards, community_cards):
    total_cards_in_hand = community_cards + private_cards # Combines all cards together
    return total_cards_in_hand
def hand_evaluation(final_hand):
    dict_ranks = {} # Stores frequency of ranks
    for a in final_hand:
        rank = a[:-1] # Extracts rank only
        if rank in dict_ranks:
             dict_ranks[rank] += 1 # Increases existing rank count
        else:
             dict_ranks[rank] = 1 # Creates new rank entry
    return dict_ranks
def pairs(evaluation):
    count = 0 # Counts number of pairs
    for t in evaluation.values():
        if t == 2:
            count += 1 # Pair found
    if count == 0:
        return 0 # No pair
    elif count == 1:
        return 1 # One pair
    elif count == 2:
        return 2 # Two pair
def three_kind(evaluation):
    count = 0
    for t in evaluation.values():
        if t == 3:
            count += 1 # Trips found
    return count 
def four_kind(evaluation):
    count = 0
    for t in evaluation.values():
        if t == 4:
            count += 1 # Quads found
    return count
def full_house(pair, three_of_a_kind):
    if three_of_a_kind >= 1 and pair >= 1:
        return 1 # Standard full house
    elif three_of_a_kind >= 2:
        return 1 # Two triplets also form full house
    else:
        return 0
def straight(final_hand):
    numeric_values = [] # Stores numeric card values
    for card in final_hand:
        rank = card[:-1] # Extract rank only
        numeric_values.append(rank_values[rank]) # Convert rank to number
    values = set(numeric_values) # Remove duplicates
    if 14 in values:
        values.add(1) # Ace can also act as low card
    for start in range(1, 11): # Check all possible straights
        needed_cards = {
            start,
            start + 1,
            start + 2,
            start + 3,
            start + 4
        }
        if needed_cards.issubset(values):
            return 1 # Straight found
    return 0
def flushes(final_hand):
    lst = {} # Stores suit frequencies
    for a in final_hand:
        suit = a[-1] # Extract suit only
        if suit in lst:
            lst[suit] += 1 # Increase suit count
        else:
            lst[suit] = 1 # Create new suit entry
    for i in lst.values():
        if i >= 5:
            return 1 # Flush found
    return 0
def straight_flushes(final_hand):
    suits = {} # Groups cards by suit
    for card in final_hand:
        suit = card[-1] # Extract suit
        if suit in suits:
            suits[suit].append(card) # Add card into suit group
        else:
            suits[suit] = [card] # Create new suit group
    for suited_cards in suits.values():
        if len(suited_cards) >= 5: # Need minimum 5 suited cards
            if straight(suited_cards) == 1:
                return 1 # Straight flush found
    return 0
def royal_flushes(final_hand):
    suits = {} # Groups cards by suit
    for card in final_hand:
        suit = card[-1] # Extract suit
        if suit in suits:
            suits[suit].append(card)
        else:
            suits[suit] = [card]
    needed = {10, 11, 12, 13, 14} # Required royal flush values
    for suited_cards in suits.values():
        numeric_values = set()
        for card in suited_cards:
            rank = card[:-1] # Extract rank only
            numeric_values.add(rank_values[rank]) # Convert to numeric value
        if needed.issubset(numeric_values):
            return 1 # Royal flush found
    return 0
def card_combinations(final_hand):
    card_combos = list(cb(final_hand,5))
    return card_combos
def score_hand(combo):
    evaluation = hand_evaluation(combo)
    pair = pairs(evaluation)
    three_of_a_kind = three_kind(evaluation)
    four_of_a_kind = four_kind(evaluation)
    f_house = full_house(pair, three_of_a_kind)
    straight_hand = straight(combo)
    flush = flushes(combo)
    straight_flush = straight_flushes(combo)
    royal_flush = royal_flushes(combo)
    if royal_flush == 1:
        return (10,)
    elif straight_flush == 1:
        suits = {}
        for card in combo:
            suit = card[-1]
            if suit in suits:
                suits[suit].append(card)
            else:
                suits[suit] = [card]
        for suited_cards in suits.values():
            if len(suited_cards) >= 5:
                numeric_values = []
                for card in suited_cards:
                    rank = card[:-1]
                    numeric_values.append(rank_values[rank])
                values = set(numeric_values)
                if 14 in values:
                    values.add(1)
                for start in range(1, 11):
                    needed_cards = {
                        start,
                        start + 1,
                        start + 2,
                        start + 3,
                        start + 4
                        }
                    if needed_cards.issubset(values):
                        return (9, start + 4)
    elif four_of_a_kind == 1:
        four_kind_values = 0
        kickers = 0
        for rank in evaluation:
            value = rank_values[rank]
            if evaluation[rank] == 4:
                four_kind_values = value
            else:
                kickers = value
        return(8,four_kind_values, kickers)
    elif f_house == 1:
        triple_value = 0
        pair_value = 0
        for rank in evaluation:
            value = rank_values[rank]
            if evaluation[rank] == 3:
                triple_value = value
            elif evaluation[rank] == 2:
                pair_value = value
        return(7,triple_value,pair_value)
    elif flush == 1:
        flush_values = []
        for card in combo:
            rank = card[:-1]
            value = rank_values[rank]
            flush_values.append(value)
        flush_values.sort(reverse=True)
        return(6, flush_values[0],flush_values[1],flush_values[2], flush_values[3],flush_values[4])
    elif straight_hand == 1:
        numeric_values = [] # Stores numeric card values
        for card in combo:
            rank = card[:-1] # Extract rank only
            numeric_values.append(rank_values[rank]) # Convert rank to number
        values = set(numeric_values) # Remove duplicates
        if 14 in values:
            values.add(1) # Ace can also act as low card
        for start in range(1, 11): # Check all possible straights
            needed_cards = {
                start,
                start + 1,
                start + 2,
                start + 3,
                start + 4
            }
            if needed_cards.issubset(values):
                return(5, start+4)
    elif three_of_a_kind == 1:
        three_kind_values = 0
        kickers = []
        for rank in evaluation:
            value = rank_values[rank]
            if evaluation[rank] == 3:
                three_kind_values = value
            else:
                kickers.append(value)
        kickers.sort(reverse=True)
        return(4,three_kind_values,kickers[0],kickers[1])
    elif pair == 2:
        pair_values = []
        kicker = 0
        for rank in evaluation:
            value = rank_values[rank]
            if evaluation[rank] == 2:
                pair_values.append(value)
            else:
                kicker = value
        pair_values.sort(reverse=True)
        return (3, pair_values[0], pair_values[1], kicker)
    elif pair == 1:
      pair_value = 0
      kickers = []
      for rank in evaluation:
          value = rank_values[rank]
          if evaluation[rank] == 2:
                pair_value = value
          else:
                kickers.append(value)
      kickers.sort(reverse=True)
      return (2, pair_value, kickers[0], kickers[1], kickers[2])
    else:
        high_card_values = []
        for card in combo:
            rank = card[:-1]
            value = rank_values[rank]
            high_card_values.append(value)
        high_card_values.sort(reverse=True)
        return (
            1,
            high_card_values[0],
            high_card_values[1],
            high_card_values[2],
            high_card_values[3],
            high_card_values[4]
            )
def best_hand(final_hand):
    combos = card_combinations(final_hand)
    best = (0,)
    for combo in combos:
        score = score_hand(combo)
        if score > best:
            best = score
    return best