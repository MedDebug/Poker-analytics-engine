from cards import rank_values, suit_names


def valid_card(card):
    rank = card[:-1]
    suit = card[-1]

    return rank in rank_values and suit in suit_names
