# -*- coding: utf-8 -*-

from utils import with_color
from operator import attrgetter

SUIT_SYMBOL = [u'\u2663', u'\u2666', u'\u2665', u'\u2660', u"", u""]

class Suits(object):
    clubs = 0 #草花
    diamonds = 1 #方片
    hearts = 2 #红桃
    spades = 3 #黑桃
    b_joker = 4 #big joker
    s_joker = 5

class Card(object):
    def __init__(self, value, suit=None):
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.value <= 10:
            temp_value = str(self.value)
        else:
            switcher = {
                11: u"J",
                12: u"Q",
                13: u"K",
                14: u"A",
                15: u"2",
                16: u"joker",
                17: u"JOKER",
            }
            temp_value = switcher.get(self.value)

        return SUIT_SYMBOL[self.suit] + temp_value

    def __cmp__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        return self.value == other.value

class CardPlay(object):
    def __init__(self, play_str):
        self.cards = []
        self.card_pattern = ''
        self.is_shunzi = False
        self.is_3dai1 = False
        self.is_3dai2 = False
        self.is_feiji = False
        self.is_zhadan = False
        self.is_duizi = False
        self.is_danzhang = False
        self.is_liandui = False
        self.is_4dai2 = False
        self.invalid = False

        __switcher = {
            '0': 10,
            '2': 15,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'J': 11,
            'j': 11,
            'Q': 12,
            'q': 12,
            'K': 13,
            'k': 13,
            'A': 14,
            's': 16,
            'b': 17,
        }

        for card_chr in play_str:
            self.cards.append(Card(__switcher.get(card_chr)))
        self.cards = sorted(self.cards, key=attrgetter('value'))
        length = len(self.cards)
        if length >= 5:
            # 三带二
            if self.cards[0] == self.cards[1] == self.cards[2]  and self.cards[3] == self.cards[4]\
                    or self.cards[0] == self.cards[1] and self.cards[2] == self.cards[3] == self.cards[4]:
                self.is_3dai1 = True
                self.card_pattern = '3dai2'
                return
            # 检查是否为顺子
            for i in range(1, length):
                card = self.cards[i]
                pre_card = self.cards[i-1]
                if card.value != pre_card.value + 1 or card.value > __switcher.get('A'):
                    break
            else:
                self.is_shunzi = True
                self.card_pattern = 'shunzi'
                return

            # 检查是否为连对
            for i in range(0, length-2, 2):
                if self.cards[i] != self.cards[i+1] or self.cards[i].value + 1 != self.cards[i+2].value:
                    break
            else:
                self.is_liandui = True
                self.card_pattern = 'liandui'
                return

            # 检查是否为飞机
            card_dict = {}
            for card in self.cards:
                if card.value in card_dict:
                    card_dict[card.value] += 1
                else:
                    card_dict[card.value] = 1

            three_count = 0
            one_count = 0
            four_count = 0
            for key in card_dict:
                if card_dict[key] == 3:
                    three_count += 1
                elif card_dict[key] == 4:
                    four_count += 1
                else:
                    one_count += card_dict[key]

            if three_count == one_count:
                self.is_feiji = True
                self.card_pattern = 'feiji'
                return

            # 检查是否为四带二
            if four_count * 2 == one_count:
                self.is_4dai2 = True
                self.card_pattern = '4dai2'
                return

        elif length == 4:
            # 检查是否为炸弹
            if self.cards[0] == self.cards[1] == self.cards[2] == self.cards[3]:
                self.is_zhadan = True
                self.card_pattern = 'zhadan'
                return

            # 检查是否为三带一
            elif self.cards[0] == self.cards[1] == self.cards[2] or self.cards[1] == self.cards[2] == self.cards[3]:
                self.is_3dai1 = True
                self.card_pattern = '3dai1'
                return

        elif length == 2:
            # 检查是否是王炸
            if (self.cards[0].value == __switcher.get('s') and self.cards[1].value == __switcher.get('b')) or \
                    (self.cards[0].value == __switcher.get('b') and self.cards[1].value == __switcher.get('s')):
                self.is_zhadan = True
                self.card_pattern = 'zhadan'
                return

            # 检查是否是对子
            elif self.cards[0] == self.cards[1]:
                self.is_duizi = True
                self.card_pattern = 'duizi'
                return

        elif length == 1:
            # 检查是否是单张
            self.is_danzhang = True
            self.card_pattern = 'danzhang'
            return

        self.invalid = True

    def get_card_pattern(self):
        return self.card_pattern


def print_cards(cards):
    pass

if __name__ == '__main__':
    play = CardPlay('44455')
    print(play.validate())
    

