from models import Juice
from models import Suica
from models import VendingMachine



def charge_to_suica(amount):
    if amount >= 100:
        suica.deposit = amount  # 正の値は残高チャージ
    else:
        print('[exeption] 100円未満のチャージはできません')

'**************************************************************'




DEFAULT_DEPOSIT = 500
PRICE_DICT = {'ペプシ': 150, 'いろはす': 120, 'モンスター': 230}

suica = Suica(DEFAULT_DEPOSIT)

# チャージ処理
input_amount = int(input('チャージする金額を入力してください（最低チャージ額: 100円） > '))
charge_to_suica(input_amount)
print(f'Suicaの残高: {suica.deposit}円')

