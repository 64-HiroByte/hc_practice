from models import Juice
from models import Suica
from models import VendingMachine


def charge_to_suica(amount):
    if amount >= 100:
        suica.deposit = amount  # 正の値は残高チャージ
    else:
        print('[exeption] 100円未満のチャージはできません')

def perchase_beverage(beverage):
    # [TODO]購入前のバリデーションチェック
    
    vending_machine.stock_dict[beverage] -= 1
    vending_machine.proceed = beverage.price  # 150は購入したジュースの値段
    suica.deposit = -beverage.price  # 150は購入したジュースの値段
    
    
'**************************************************************'

'''
- ✅自動販売機の在庫取得 -> vending_machineのgetterで設定すればよい
- 自動販売機の売り上げ金額の取得 -> vending_machineのgetterで設定すればよい

- ジュースの一覧表示（在庫も含む）
- 購入処理（validation）
    - Suicaの残高が足りているか ->exception
    - ジュースの在庫は0でないか -> exception
- 購入処理
    - 購入されたジュースの在庫を-1
    - 売り上げ金額にジュースの値段を足す
    - Suicaのチャージ額からジュースの値段を差し引く
- 補充処理
    - 自動販売機に在庫を補充して、任意のジュースの在庫を増やす
'''



DEFAULT_DEPOSIT = 500
# PRICE_DICT = {'ペプシ': 150, 'いろはす': 120, 'モンスター': 230}
# default_stock = {'ペプシ': 5, }  # [TODO] 機能拡張で全商品の在庫を５にする

# インスタンス化
suica = Suica(DEFAULT_DEPOSIT)
vending_machine = VendingMachine(default_stock)

pepsi = Juice(_name='ペプシ', price=150)
monster = Juice(_name='モンスター', price=230)
ilohas = Juice(_name='いろはす', price=120)


# print(vending_machine.proceed, vending_machine.stock_dict)


# # チャージ処理
# input_amount = int(input('チャージする金額を入力してください（最低チャージ額: 100円） > '))
# charge_to_suica(input_amount)

# # 購入
# perchase_beverage('ペプシ')
# print(vending_machine.stock_dict)
# print(vending_machine.proceed)
# print(suica.deposit)
