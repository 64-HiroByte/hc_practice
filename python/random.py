import os
import sys
# カレントディレクトリのパスを取得し、sys.pathからカレントディレクトリを削除
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if p != current_dir]

# 標準ライブラリのrandomモジュールをインポート
import random


def create_group(members, min=2, max=3):
    """
    引数membersから無作為に抽出した人で新たなグループを作成する関数
    グループを構成する人数は任意に指定できる

    Args:
        members (list): グループのメンバーリスト
        min (int, optional): グループを構成する最少人数 (デフォルト値は 2)
        max (int, optional): グループを構成する最多人数 (デフォルト値は 3)

    Returns:
        list: 無作為に抽出した人で構成されたグループ。
    """
    # maxまたはminに渡された値のバリデーション
    if max > len(members) or min < 1:
        return
        
    random.shuffle(members)
    num = random.randint(min, max)
    group = random.sample(members, num)
    return group

members = ['A', 'B', 'C', 'D', 'E', 'F']

first_group = create_group(members)

second_group = [member for member in members if member not in first_group]

print(sorted(first_group))
print(sorted(second_group))
