# -*- coding: utf-8 -*-

from operator import attrgetter
from random import choice

STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },
        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },
        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },
        'default' :
        {
            'end' : 0,
        },
}

def with_color(string, mode='', fore='', back=''):

    if fore:
        fore = str(STYLE['fore'][fore])
    if back:
        back = str(STYLE['back'][back])
    if mode:
        mode = str(STYLE['mode'][mode])
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end   = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)# -*- coding: utf-8 -*-

def print_cards(player):
    cards = player.cards
    cards = sorted(cards, key=attrgetter('value'))
    print(player.username, end=':')
    color = 'red'
    for card in cards:
        if  (cards.index(card) != 0) and (card != cards[cards.index(card)-1]):
            color = choice(list(STYLE['fore'].keys()))
            # print('change', end='')
        print(with_color(card, fore=color), end=' ')
           #TODO why  
    print()


def new_replace(cards): 
    """type(cards) = list 
    a,A -> 14
    j,J -> 11
    ...
    """
    cards = [ c.replace('0','10').replace('a','14').replace('A','14').replace('2','15').\
    replace('2','15').replace('j','11').replace('J','11')\
    .replace('q','12').replace('Q','12').replace('k','13').replace('k','13').replace('s','16').replace('b','17').replace('boom','9999')
     for c in cards]
    return cards