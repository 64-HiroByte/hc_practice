import os
import string

# import controller


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

