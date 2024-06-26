import view
from models import Juice
from models import Suica
from models import VendingMachine


# modeを選択 [0: Suicaにチャージ / 残高照会, 1: ジュースの購入, 2: ジュースの補充]
def mode_select():
    # view.pyの関数を指定: 画面表示 > 標準入力 >バリデーションチェック > 入力値をリターン
    
    
    return


# Suicaへ入金
def charge_to_suica(deposit):
    if deposit >= 100:
        suica.add_balance(deposit)  # 正の値は残高チャージ
    else:
        print('[exeption: small deposit error] 100円未満のチャージはできません')


def create_juice(i, juice_list, num):
    """_summary_

    Args:
        i (int): juice_listを表示して、input()によって標準入力された値
        juice_list (list): 使用可能なジュースの名前と値段のlist
        num (int): 作成するジュースの本数
    """
    created_juice = [Juice(name=juice_list[i][0], price=juice_list[i][1]) for _ in range(num)]
    return created_juice


def perchase_juice(i, juice_list, suica):
    # [TODO]購入前のバリデーションチェック
    
    # 購入可能な場合の処理
    # 前提： JUICE_LISTをview.pyで表示させて、標準入力されたJUICE＿LISTのindex No（i）を使用する
    print(f'購入前のSuicaの残高 {suica.show_balance()}')
    perchased_juice = vending_machine.inventory[i].pop(0)  # pop()によって在庫は1本減る
    
    suica.add_balance(-perchased_juice.price) 
    print(f'購入後のSuicaの残高 {suica.show_balance()}')
    print(f'購入前の自販機の売上金合計 {suica.show_balance()}')
    vending_machine.add_proceeds(perchased_juice.price)
    print(f'購入後の自販機の売上金合計 {suica.show_balance()}')
    
    
# 初期設定
DEFAULT_DEPOSIT = 500
JUICE_LIST = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)] # nameはJUICE_LIST[i][0], priceはJUICE_LIST[i][1]
DEFAULT_NUM = 5

# 在庫管理用のリストを生成
inventoty = []
for i in range(len(JUICE_LIST)):
    created_list = create_juice(i=i, juice_list=JUICE_LIST, num=DEFAULT_NUM)
    inventoty.append(created_list)

# SuicatとVendingMachineクラスのインスタンス化
suica = Suica(DEFAULT_DEPOSIT)
vending_machine = VendingMachine(inventoty)

# [0]:Suicaのチャージ / [1]: ジュースの購入 / [2]: ジュースの補充から選択

# [0]: Suicaのチャージ

print(f'現在の残高は {suica.show_balance()} 円です。')  # view.py or templates/template.txtへ
txt = 'Suicaへのチャージ金額を入力してください（最低チャージ額: 100円） > '  # view.py or templates/template.txtへ

deposit = input_value_validation(txt)

charge_to_suica(deposit=deposit)
print(f'現在の残高は {suica.show_balance()} 円です。')


# [1]: ジュースの購入



# [2]: ジュースの補充