import sys


def get_load_data():
    f = sys.stdin
    load_data = []
    for line in f:
        line = line.replace('\n', '')
        str_list = line.split(',')
        load_data.append([int(d) for d in str_list])
    return load_data

load_data = get_load_data()
regulation_shots = load_data[0]
my_shots = load_data[1]

SCORE_NAMES = ('ホールインワン', 'コンドル', 'アルバトロス', 'イーグル', 'バーディ')

SCORE_NAME_DICT = {
    'par_3': (SCORE_NAMES[0], SCORE_NAMES[-1]),
    'par_4': (SCORE_NAMES[0], SCORE_NAMES[-2], SCORE_NAMES[-1]),
    'par_5': SCORE_NAMES[1:],
}


for i in range(len(regulation_shots)):
    deff = my_shots[i] - regulation_shots[i]
    if deff > 0:
        if deff == 1:
            my_score = 'ボギー'
        else:
            my_score = f'{deff}ボギー'
    elif deff == 0:
        my_score = 'パー'
    else:
        my_score = SCORE_NAME_DICT[f'par_{regulation_shots[i]}'][deff]
    
    print(f'index: {i}, regulation: {regulation_shots[i]}, my_shot:{my_shots[i]}, my_score: {my_score}')

