from random import choice


def main():

    cards = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }

    print("Player's Turn-----------------------")

    card, person_points = deal_card(cards=cards, total_points=0)
    print("Card drawn:", card, ", Player's Total:", person_points)

    card, person_points = deal_card(cards, person_points)
    print("Card drawn:", card, ", Player's Total:", person_points)

    person_points = dealing_logic(cards=cards,
                                  is_dealer=False,
                                  total_points=person_points,
                                  deal_threshold=21)

    print("Dealer's Turn-----------------------")

    card, dealer_points = deal_card(cards=cards, total_points=0)
    print("Card drawn:", card, ", Dealer's Total:", dealer_points)

    card, dealer_points = deal_card(cards=cards, total_points=dealer_points)
    print("Card drawn:", card, ", Dealer's Total:", dealer_points)

    dealing_logic(cards=cards,
                  is_dealer=True,
                  total_points=dealer_points,
                  deal_threshold=17,
                  winning_threshold=person_points)


def deal_card(cards, total_points):
    single_card = choice(list(cards.keys()))
    total_points += cards[single_card]
    return single_card, total_points


def dealing_logic(cards, is_dealer, total_points, deal_threshold, winning_threshold=21):

    while True:

        if total_points == 21:
            if is_dealer:
                print("Blackjack, dealer has won!")
            else:
                print("Blackjack, you have won!")
            exit()
        elif total_points > 21:
            if is_dealer:
                print("Bust, Dealer has lost!")
            else:
                print("Bust, You have lost!")
            exit()
        elif is_dealer and total_points > winning_threshold:
            print("Dealer has won")
            exit()
        elif total_points < deal_threshold:
            if is_dealer:
                card, total_points = deal_card(cards=cards, total_points=total_points)
                print("Card drawn:", card, ", Dealer's Total:", total_points)
            else:
                should_deal = input("Want another card? [y/n]: ")
                if should_deal.lower() == "y":
                    card, total_points = deal_card(cards, total_points)
                    print("Card drawn:", card, ", Player's Total:", total_points)
                else:
                    break

    return total_points


main()
