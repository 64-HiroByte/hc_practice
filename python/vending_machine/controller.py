import view
from models import Juice
from models import Suica
from models import VendingMachine


# Suicaへ入金
def deposit_to_suica(deposit):
    if deposit >= 100:
        suica.add_balance(deposit)  # 正の値は残高チャージ
    else:  # [TODO] 独自例外の作成（myexceptions.py）
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


# 在庫状況の取得  --> method?
def get_stock_lists(juice_lists):
    """
    juice_listsと自動販売機に格納されているジュースオブジェクトの数から在庫本数を取得する関数

    Args:
        juice_lists (list): ジュースの名前と値段の組み合わせ（tuple）を格納したリスト

    Returns:
        list: ジュースの名前と在庫本数のリストを格納したリスト
    """    
    stock_lists = []
    for i in range(len(juice_lists)):
        stock_list = [juice_lists[i][0], len(vending_machine.stocks[i])]
        stock_lists.append(stock_list)
    return stock_lists  


def is_purchasable(price):
    """
    引数priceとSuicaの残高を比較して購入可能か判定する

    Args:
        price (int): _description_

    Returns:
        bool: _description_
    """    
    if suica.show_balance() < price:
        return False
    else:
        return True


def charge_to_suica(suica):
    # while True:
    input_deposit = view.input_deposit(suica)
    deposit_to_suica(input_deposit)
    
    # 入金後のSuicaの残高を表示
    view.show_suica_balance(suica)
    
    # [TODO] whileループするならbreakの条件を追記


# ジュースの購入操作: whileループ
def purchase_juice(juice_lists, min_price):
    # while True:
    
# Suicaの残高とジュースの在庫表示
    view.show_suica_balance()
    view.show_stock_lists(juice_lists)
    
# Suicaの残高から購入可能か判定
    purchasable = is_purchasable(min_price)
    if not purchasable:
        print(f'Suicaの残高が不足しています。最低でも{min_price}円以上の残高が必要です')
        # break
    
# 購入処理
    txt = '購入したいジュースの番号を入力してください > '
    i = view.choose_juice(juice_lists, txt)  # 選択したjuice_listsのindex番号 iを取得
    perchased_juice = vending_machine.stocks[i].pop(0)  # pop()によって在庫は1本減る
    
# Suicaの残高から支払い
    print(f'購入前のSuicaの残高 {suica.show_balance()}')
    suica.add_balance(-perchased_juice.price)  # ジュースの購入額をSuicaの残高から差し引く
    print(f'購入後のSuicaの残高 {suica.show_balance()}')
    
# 自動販売機に売上額を計上
    print(f'購入前の自販機の売上金合計 {vending_machine.show_balance()}')
    vending_machine.add_proceeds(perchased_juice.price)
    print(f'購入後の自販機の売上金合計 {vending_machine.show_balance()}')
    
    # [TODO] ループするか、モード選択に戻るかの選択 -> view.pyの処理


# ジュースの補充: whileループ
def replenish_juice(juice_lists):
# 在庫状況の取得
    view.show_stock_lists(juice_lists)
    
# [TODO] 補充したいジュースの選択と本数の入力 --> view.py
    txt = '補充するジュースの番号を入力してください > '
    i = view.choose_juice(juice_lists, txt)
    num = input('補充する本数を入力してください > ') # [TODO] 関数化する
    # 補充するジュースの生成(引数i, numはview.pyの関数実行時の返り値)
    replenish_juice = create_juice(i, juice_lists, num)
    
    # [TODO] 自動販売機の在庫に生成したジュースを追加　--> extend()を使用する
    
    # [TODO] ループするか、モード選択に戻るかの選択 -> view.pyの処理


# modeを選択 [0: Suicaにチャージ / 残高照会, 1: ジュースの購入, 2: ジュースの補充]
def mode_select(options):
    # view.pyの関数を指定: 画面表示 > 標準入力 >バリデーションチェック > 入力値をリターン
    users_choice = view.is_selectable(options)
    if users_choice == 'q':
        print('Good bye!!')
    
    return users_choice


# 初期設定
DEFAULT_DEPOSIT = 500
JUICE_LISTS = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)]
DEFAULT_NUM = 5
MODE_OPTIONS = ('Suicaにチャージ', 'ジュースの購入', 'ジュースの補充')

# 最も安いジュースの価格
min_price = min([juice[1] for juice in JUICE_LISTS])

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
    charge_to_suica()

# [1]: ジュースの購入
if mode == '1':
    purchase_juice(i, JUICE_LISTS)


# [2]: ジュースの補充