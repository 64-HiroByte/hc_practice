import view
from models import Juice
from models import Suica
from models import VendingMachine


# Suicaへ入金
def charge_to_suica(deposit):
    if deposit >= 100:
        suica.add_balance(deposit)  # 正の値は残高チャージ
    else:
        print('[exeption: small deposit error] 100円未満のチャージはできません')


# ジュースインスタンスの生成
def create_juice(i, juice_lists, num):
    """
    juice_listsに格納されているジュースを選択して任意の本数インスタンス化する関数

    Args:
        i (int): juice_listsを表示して、標準入力された値（インデックス番号）
        juice_lists (list): 使用可能なジュースの名前と値段のlist
        num (int): 作成するジュースの本数
    """
    created_juice = [Juice(name=juice_lists[i][0], price=juice_lists[i][1]) for _ in range(num)]
    
    return created_juice


# 在庫状況の取得
def get_stock_lists(juice_lists):
    stock_lists = []
    for i in range(len(juice_lists)):
        stock_list = [juice_lists[i][0], len(vending_machine.stocks[i])]
        stock_lists.append(stock_list)
    return stock_lists  


# ジュースの購入操作
def perchase_juice(juice_lists):
    # [TODO]購入前のバリデーションチェック
    min_price = min([juice[1] for juice in juice_lists])
    if suica.__balance < min_price:
        print(f'Suicaの残高が不足しています。最低でも{min_price}円以上の残高が必要です')
    stock_lists = get_stock_lists(juice_lists)
    
    # 購入可能な場合の処理
    # 前提： JUICE_LISTSをview.pyで表示させて、標準入力されたJUICE＿LISTSのindex No（i）を使用する
    print(f'購入前のSuicaの残高 {suica.show_balance()}')
    perchased_juice = vending_machine.stocks[i].pop(0)  # pop()によって在庫は1本減る
    
    suica.add_balance(-perchased_juice.price) 
    print(f'購入後のSuicaの残高 {suica.show_balance()}')
    print(f'購入前の自販機の売上金合計 {suica.show_balance()}')
    vending_machine.add_proceeds(perchased_juice.price)
    print(f'購入後の自販機の売上金合計 {suica.show_balance()}')


# ジュースの補充
def replenish_juice(juice_lists):
    
        
    # ジュースの選択と本数の入力
    
    # 自動販売機に補充
    create_juice(i, juice_lists, num)

# modeを選択 [0: Suicaにチャージ / 残高照会, 1: ジュースの購入, 2: ジュースの補充]
def mode_select(options):
    # view.pyの関数を指定: 画面表示 > 標準入力 >バリデーションチェック > 入力値をリターン
    users_choice = view.is_selectable(options)
    if users_choice == 'q':
        print('Good bye!!')
    
    return users_choice


# 初期設定
DEFAULT_DEPOSIT = 500
JUICE_LISTS = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)] # nameはJUICE_LIST[i][0], priceはJUICE_LIST[i][1]
DEFAULT_NUM = 5
MODE_OPTIONS = ('Suicaにチャージ', 'ジュースの購入', 'ジュースの補充')

# 在庫管理用のリストを生成
stocks = []
for i in range(len(JUICE_LISTS)):
    created_list = create_juice(i=i, juice_lists=JUICE_LISTS, num=DEFAULT_NUM)
    stocks.append(created_list)

# SuicatとVendingMachineクラスのインスタンス化
suica = Suica(DEFAULT_DEPOSIT)
vending_machine = VendingMachine(stocks)

# [0]:Suicaにチャージ / [1]: ジュースの購入 / [2]: ジュースの補充から選択
mode = mode_select(MODE_OPTIONS)


# [0]: Suicaにチャージ
if mode == '0':
    print(f'現在の残高は {suica.show_balance()} 円です。')  # view.py or templates/template.txtへ
    txt = 'Suicaにチャージする金額を入力してください（最低チャージ額: 100円） > '  # view.py or templates/template.txtへ

    deposit = view.input_value_validation(txt)

    charge_to_suica(deposit=deposit)
    print(f'現在の残高は {suica.show_balance()} 円です。')

# [1]: ジュースの購入
if mode == '1':
    # ジュースの名前と在庫本数の表示
    
    # ジュースの購入処理
    perchase_juice(i, JUICE_LISTS)


# [2]: ジュースの補充