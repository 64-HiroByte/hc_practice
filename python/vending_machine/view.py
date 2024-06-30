import os
import string

import controller
from controller import suica
from controller import vending_machine


# input()のバリデーションチェック int型か判定　
def input_value_validation(txt):
    while True:
        try:
            input_value = int(input(txt))
        except ValueError:
            print('[ValueError] 正しい値を入力してください')
            continue
        else:
            break
    return input_value


# input()のバリデーションチェック　選択肢から選択しているか判定
def is_selectable(options):
    while True:
        # 選択肢（options）を表示
        print('ここでは、Suicaにチャージ / ジュースの購入 / ジュースの補充 を選択できます\n選択肢の番号を選んでください')
        user_input = input('番号を入力してください > ')
        if user_input in options:
            break
        else:
            print('選択肢の中から選んでください')
        
    return user_input


# Suicaの残高表示
def show_suica_balance():
    balance = suica.show_balance()
    print(f'現在の残高は {balance} 円です')


# Suicaに入金する金額を入力するための関数
def input_deposit():
    show_suica_balance()
    txt = 'Suicaにチャージする金額を入力してください（最低チャージ額: 100円） > '
    return input_value_validation(txt)


# ジュースと在庫本数の表示
def show_stock_lists(juice_lists):
    stock_lists = controller.get_stock_lists(juice_list)
    for i, juice_list in enumerate(zip(juice_lists, stock_lists)):
        print(f'{i} : {juice_list[0][0]} （{juice_list[0][1]}円）    残り {juice_list}本')


def choose_juice(juice_lists, txt):
    # 自動販売機の在庫リスト表示
    show_stock_lists(juice_lists)
    
    # 購入したいジュースの選択
    
    juice_lists_index = input(txt)
    input_value_validation()
    
    return juice_lists_index


# [TODO] 標準入力するための関数を作成する（arg: ｔｘｔ）
def your_input(txt):
    '''
    用途
    - モードを選択するための番号入力
    - Suicaのチャージ額を入力
    - 購入 / 補充したいジュースのindex番号を入力
    - 補充するジュースの本数を入力
    '''
    pass