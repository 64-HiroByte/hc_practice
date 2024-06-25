from models import Juice
from models import Suica
from models import VendingMachine

# input()のバリデーションチェック int型か判定　 -- views.pyで呼び出す
def input_value_validation(input_value):
    try:
        return int(input_value)
    except ValueError:
        print('正しい値を入力してください')
    
    
# input()のバリデーションチェック　選択肢から選択しているか判定 -- views.pyで呼び出す
def selectable_validation(input_value, options):
    try:
        if input_value in options:
            return input_value
    except:
        print('選択肢の中から選んでください')


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


def perchase_beverage(beverage):
    # [TODO]購入前のバリデーションチェック
    
    vending_machine.inventory[beverage] -= 1
    vending_machine.proceed = beverage.price  # 150は購入したジュースの値段
    suica.deposit = -beverage.price  # 150は購入したジュースの値段
    
    
# 初期設定
DEFAULT_DEPOSIT = 500
JUICE_LIST = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)] # nameはJUICE_LIST[i][0], priceはJUICE_LIST[i][1]
DEFAULT_NUM = 5

# 在庫管理用のリストを生成
inventoty = []
for i in range(len(JUICE_LIST)):
    created_list = create_juice(i=i, juice_list=JUICE_LIST, num=DEFAULT_NUM)
    inventoty.append(created_list)

# インスタンス化
suica = Suica(DEFAULT_DEPOSIT)
vending_machine = VendingMachine(inventoty)



# print(vending_machine.proceed, vending_machine.stock_dict)


# # チャージ処理
# input_amount = int(input('チャージする金額を入力してください（最低チャージ額: 100円） > '))
# charge_to_suica(input_amount)

# # 購入
# perchase_beverage('ペプシ')
# print(vending_machine.stock_dict)
# print(vending_machine.proceed)
# print(suica.deposit)
