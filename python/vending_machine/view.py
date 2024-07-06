import os
import string


# 標準入力するための関数
def input_num(txt):
    '''
    用途
    - モードを選択するための番号入力
    - Suicaのチャージ額を入力
    - 購入 / 補充したいジュースのindex番号を入力
    - 補充するジュースの本数を入力
    '''
    input_value = input(f'{txt} > ')
    # ここにバリデーションチェックいれるか検討
    
    return input_value

def show_message(sep_line='', sentence='', additional_msg=''):
    print(f'{sep_line}\n{additional_msg}{sentence}')

# 標準入力した値が選択肢に含まれているか判定する関数
def get_selected_option(options, sep_line='', quit='q'):
    selectable_num = [quit]
    show_options = sep_line
    
    for i, option in enumerate(options):
        selectable_num.append(str(i))
        show_options += f'\n{i} : {option}'
    print(f'ここでは {" / ".join(options)} を選択できます')

    while True:
        print(show_options)
        selected_option = input(f'\n番号を入力してください（戻る場合は "{quit}" を入力） > ')
        if selected_option in selectable_num:
            break
        else:
            print('\n選択肢の中から番号を選んでください' )
        
    return selected_option


# input()のバリデーションチェック int型か正の値か判定　
def input_value_validation(txt, quit='q'):
    while True:
        input_value = input(txt)
        if input_value == quit:
            break
        try:
            input_value = int(input_value)
            if input_value <= 0:
                raise ValueError
        except ValueError:
            print('[ValueError] 正しい値を入力してください')
            continue
        else:
            break
    return input_value


# Suicaに入金する金額を入力するための関数
def input_deposit(min_deposit, quit='q'):
    txt = f'Suicaにチャージする金額を入力してください\n（最低チャージ額: {min_deposit}円, 前に戻る: "{quit}"） > '
    return input_value_validation(txt)


# ジュースと在庫本数の表示
def show_stock_lists(juice_lists, stock_lists):
    # stock_lists = controller.get_stock_lists(juice_list) 変数stock_listsは渡すべきもの
    for i, juice_list in enumerate(zip(juice_lists, stock_lists)):
        print(f'{i} : {juice_list[0][0]} （{juice_list[0][1]}円）    残り {juice_list}本')


def choose_juice(juice_lists, txt):
    # 自動販売機の在庫リスト表示
    show_stock_lists(juice_lists)
    
    # 購入したいジュースの選択
    
    juice_lists_index = input(txt)
    input_value_validation()
    
    return juice_lists_index


