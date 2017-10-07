# -*- coding: utf-8 -*-

from utils import new_replace, print_cards

from card import CardPlay

class Player(object):
    def __init__(self, username, playerid, tableid):
        self.username = username
        self.playerid = playerid
        self.tableid = tableid
        self._cards = []

    def __str__(self):
        return self.username

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        #validate cards
        self._cards = value


    def play(self, last_hand=None):
        """出牌 检测出牌是否在手牌中"""
        
        legal_card = [ str(c) for c in range(3,18) ]
    
        for i in range(0,100):
            cards_on_hand = [ str(card.value) for card in self._cards ]
            flag = 0
            print_cards(self)
            card_play = input('{} 出牌:'.format(self.username))
            if len(card_play.strip()) == 0 or card_play.strip() == 'pass':
                return True
            temp = list(card_play)
            if card_play.strip() == 'show':
                print_cards(self)
                continue
            card_play = new_replace(list(card_play)) 
            print(card_play)
            for card in card_play: 
                if card not in legal_card:
                    print('不合法字符')
                    flag = 1
                    break
            if flag == 1:continue

            for card in card_play: 
                if card not in cards_on_hand:
                    print('你没有牌')
                    flag = 1
                    break
                else:
                    cards_on_hand.remove(card)
            if flag == 1:continue

            play = CardPlay(temp)
            card_pattern = play.get_card_pattern()
            print(card_pattern)
            if not card_pattern:continue
            print(card_pattern+':'+'-'.join(temp))
            self.remove_after_play(card_play)
            return True

    def remove_after_play(self, card_play):
        card_play = [ int(c) for c in card_play ]
        for play_card in card_play:
            self.cards.remove([cc for cc in self.cards if cc.value == play_card][0])



