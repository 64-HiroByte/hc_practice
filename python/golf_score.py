import sys


def get_load_data():
    """
    catコマンドにより標準出力されたデータを受取り、データをリストに格納する関数
    標準出力されるデータは、1行目に規定打数、2行目に打数が入力されている

    Returns:
        list: 2次元リスト[[規定打数(int)], [打数(int)]]
    """    
    f = sys.stdin
    load_data = []
    for line in f:
        line = line.replace('\n', '')
        str_list = line.split(',')
        load_data.append([int(d) for d in str_list])
    return load_data


def loaded_data_validation(reguration_shots, my_shots):
    """
    get_load_data()によって出力されたデータのバリデーションチェックを行う関数
    リストのデータ数を比較し、データ数が不一致の場合はexitする

    Args:
        reguration_shots (list): 規定打数のリスト(int)
        my_shots (list): 打数のリスト(int)
    """    
    if len(reguration_shots) != len(my_shots):
        sys.exit('データ数が一致しません')


def get_my_scores(regulation_shots, my_shots, score_name_dict):
    """
    プレイヤーの打数に応じてスコアの名称を判定し、リストに格納する関数

    Args:
        regulation_shots (tuple): 規定打数のリスト(int)
        my_shots (tuple): 打数のリスト(int)
        score_name_dict (dict): 規定打数とスコア名称の辞書

    Returns:
        list: 打数に応じたスコア名称
    """
    my_scores = []
    for i in range(len(regulation_shots)):
        deff = my_shots[i] - regulation_shots[i]
        if deff > 0:
            my_score = 'ボギー' if deff == 1 else f'{deff}ボギー'
        elif deff == 0:
            my_score = 'パー'
        else:
            my_score = score_name_dict[f'par_{regulation_shots[i]}'][deff]
        my_scores.append(my_score)
    return my_scores


if __name__ == '__main__':
    SCORE_NAMES = ('ホールインワン', 'コンドル', 'アルバトロス', 'イーグル', 'バーディ')

    SCORE_NAME_DICT = {
        'par_3': (SCORE_NAMES[0], SCORE_NAMES[-1]),
        'par_4': (SCORE_NAMES[0], SCORE_NAMES[-2], SCORE_NAMES[-1]),
        'par_5': SCORE_NAMES[1:],
    }

    # 規定打数のリストと打数のリストの生成
    load_data = get_load_data()
    regulation_shots = load_data[0]
    my_shots = load_data[1]

    # 生成したリストのバリデーションチェック
    loaded_data_validation(regulation_shots, my_shots)

    # スコア名称の判定と結果の出力
    my_scores = get_my_scores(regulation_shots, my_shots, SCORE_NAME_DICT)
    print(','.join(my_scores))
