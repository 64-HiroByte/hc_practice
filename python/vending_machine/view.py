import controller


# input()のバリデーションチェック int型か判定　 -- views.pyで呼び出す
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


# input()のバリデーションチェック　選択肢から選択しているか判定 -- views.pyで呼び出す
def is_selectable(options):
    while True:
        # 選択肢（options）を表示
        
        user_input = input('選択肢から選んでください > ')
        if user_input in options:
            break
        else:
            print('選択肢の中から選んでください')
        
    return user_input