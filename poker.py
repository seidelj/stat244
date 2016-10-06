import random

def get_deck():
    Rank = 'akqj098765432'
    Suit = 'dhsc'

    deck = []
    for s in Suit:
        for r in Rank:
            card = s+r
            deck.append(card)
    return deck

num = 0
den = 0
for x in range(0,1000000):
    deck = get_deck()
    random.shuffle(deck)
    p1 = []
    p2 = []
    p3 = []
    p1.append(deck.pop())
    p2.append(deck.pop())
    p3.append(deck.pop())
    p1.append(deck.pop())
    p2.append(deck.pop())
    p3.append(deck.pop())

    if p1[0][1] != p1[1][1] and p2[0][1] != p2[1][1] and p3[0][1] != p3[1][1]:
        num +=1
    den +=1

print float(num)/den
