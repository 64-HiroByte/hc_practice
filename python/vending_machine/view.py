def show_message(sep_line='', main_msg='', additional_msg=''):
    """メッセージを標準出力する

    Args:
        sep_line (str, optional): 仕切り線（初期値 ''）
        main_msg (str, optional): メインのメッセージ（初期値 ''）
        additional_msg (str, optional): 追加のメッセージ（初期値 ''）
    """    
    print(f'{sep_line}\n{additional_msg}{main_msg}')


# input()のバリデーションチェック int型か正の値か判定　
def input_value_validation(txt, quit='q'):
    """標準入力された値のバリデーションチェックと取得

    Args:
        txt (str): 標準入力時に表示させる文字列
        quit (str, optional): 前の画面に戻る時に入力するコマンド（初期値 'q'）

    Raises:
        ValueError: intに型変換できない、または負の値が入力された場合（quitコマンドを除く）

    Returns:
        int: 正の整数
    """    
    while True:
        input_value = input(txt)
        if input_value == quit:
            break
        try:
            input_value = int(input_value)
            if input_value <= 0:
                raise ValueError
        except ValueError:
            print('\nValueError: 正しい値を入力してください\n')
            continue
        else:
            break
    return input_value


# Suicaに入金する金額を入力するための関数
def input_deposit(min_deposit, quit='q'):
    """Suicaにチャージする金額の入力

    Args:
        min_deposit(int): Suicaへの最少入金額
        quit (str, optional): 前の画面に戻る時に入力するコマンド（初期値 'q'）

    Returns:
        int: Suicaにチャージする金額（正の値）
    """
    txt = f'Suicaにチャージする金額を入力してください\n（最低チャージ額: {min_deposit}円, 前に戻る: "{quit}"） > '
    return input_value_validation(txt)


# 標準入力した値が選択肢に含まれているか判定する関数
def input_selected_option(options, msg, sep_line='', quit='q'):
    """選択肢から任意のインデックス番号を選択する

    Args:
        options (list): 選択肢を格納したリスト
        msg (str): 選択肢と一緒に表示するメッセージ
        sep_line (str, optional): 仕切り線（初期値 ''）
        quit (str, optional): 前の画面に戻る時に入力するコマンド（初期値 'q'）
        
    Returns:
        str: 選択した選択肢のインデックス番号（文字列）またはquitコマンド
    """
    selectable_num = [quit]
    show_options = sep_line + msg
    
    # 選択肢のインデックス番号と選択肢を表示する文字列
    for i, option in enumerate(options):
        selectable_num.append(str(i))
        show_options += f'\n{i} : {option}'
    
    # quitコマンドまたは選択肢のインデックス番号に合致するまでループ
    while True:
        print(show_options)
        selected_option = input(f'\n番号を入力してください（戻る場合は "{quit}" を入力） > ')
        if selected_option in selectable_num:
            break
        else:
            print('\n選択肢の中から番号を選んでください\n' )
        
    return selected_option


def input_yes_or_no(txt):
    """反復処理を実行するか確認する

    Args:
        txt (str): 反復処理の確認メッセージ

    Returns:
        str: 'y'または'n'
    """    
    result = ''
    while result != 'y' and result != 'n':
        result = input(txt + '（y/n） > ').lower()
    return result