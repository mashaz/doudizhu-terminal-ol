# -*- coding: utf-8 -*-

from random import shuffle, randint
from card import Card
from player import Player

class Table(object):
    player_sitted = []
    player_and_card = {}
    def __init__(self, tableid):
        self.tableid = tableid
        self.player_sum = 0

    def is_full(self):
        return bool(self.player_sum == 3)

    def sit_down(self, player):
        if player in self.player_sitted:
            print(player, 'already sitted down.')
            return
        self.player_sitted.append(player)
        self.player_sum += 1
        print(player,'sit down')
    
    def leave(self):
        pass

    def clear(self):
        pass

    def start_game(self):
        if len(self.player_sitted) != 3:
            return 
        cards = init_shuffle_cards()
        for i in range(0, 17):
            for p in self.player_sitted:
                p.cards.append(cards.pop())

        print('底牌: ', end=' ')
        for card in cards:
            # print(card)
            print(u'\u2588', end=' ')
        print()
    def is_anyone_empty(self):
        return False

def init_shuffle_cards():
    cards = []
    for i in range(3, 16):
        for j in range(0, 4):
            cards.append(Card(i, j))
    cards.append(Card(16, 4))
    cards.append(Card(17, 5))
    shuffle(cards)
    shuffle(cards)
    shuffle(cards)
    # for card in cards:
    #    print(card, end=' ')
    return cards
