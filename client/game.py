#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
玩家类player
纸牌类card
游戏桌类table 发牌
"""

from utils import with_color, print_cards
from card import CardPlay
from player import Player
from table import Table
from random import randint

import ipdb

if __name__ == '__main__':
    table = Table(tableid=1)

    player1 = Player('笑面虎',1,1)
    table.sit_down(player1)
    player2 = Player('张飞卖肉',2,1)
    player3 = Player('常山赵子龙',3,1)
    table.sit_down(player2)
    table.sit_down(player3)
    table.sit_down(player3)

    if table.is_full():
        table.start_game()

    # print_cards(player1)
    # print_cards(player2)
    # print_cards(player3)
    cards_on_deck = []
    record = []
    while 1:
        record = player1.play(record)
        record = player2.play(record)
        record = player3.play(record)
        if table.is_anyone_empty():
            break

