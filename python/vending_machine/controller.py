# import view
# from models import Juice
from models import Suica
from models import VendingMachine


# ジュースインスタンスの生成
# def create_juice(i, juice_lists, num):
#     """
#     juice_listsに格納されているジュースを選択して任意の本数インスタンス化する関数

#     Args:
#         i (int): juice_listsを表示して、標準入力された値（インデックス番号）
#         juice_lists (list): 使用可能なジュースの名前と値段のlist
#         num (int): 生成するジュースの本数
#     """
#     created_juice = [Juice(name=juice_lists[i][0], price=juice_lists[i][1]) for _ in range(num)]
    
#     return created_juice


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


def get_balance_sentence(sep_line=''):
    return f'{sep_line}現在のSuicaの残高は {suica.balance}円 です\n'


def charge_to_suica(sep_line='', quit='q'):
    while True:
        '''
        Suicaにチャージを選択した場合の処理フロー
            1. 現在のSuicaの残高を表示
            2. 入金額を入力
            3. 入力値のバリデーションチェック（intに変換できるか、負の値ではないか）
            ---- ここまでwhileループ処理 ----
            
            4. Suicaの残高に加算
            5. 加算後のSuicaの残高を表示
        '''
        # 1. 現在のSuicaの残高を取得
        balance_sentece = get_balance_sentence(sep_line=sep_line)
        before_deposit = suica.balance
        
        # 2. 入金額を入力
        input_value = view.input_deposit(balance_sentece)
        
        # quit（q）が入力された場合の処理
        if input_value == quit:
            break
        
        suica.balance = input_value
        if suica.balance > before_deposit:
            print(get_balance_sentence(sep_line=sep_line))
            break


# ジュースの購入操作: whileループ
def purchase_juice(juice_lists, sep_line=''):
    '''
    - ジュースを選択
        - Suicaの残高は十分か --> 例外発生させる
        - 在庫のある商品か --> 例外発生させる
    
    - 選択した商品の在庫を-1
    - 選択した商品代金をSuicaから差し引く
    - 選択した商品代金を自販機の売上に計上
    - （ステータス表示）
    '''
    # 自販機で扱うジュースの最低価格を取得
    min_price = min([juice[1] for juice in juice_lists])
    
    while True:
        # Suicaの残高とジュースの在庫の取得、変数に代入
        balance = suica.balance
        balance_sentence = get_balance_sentence(sep_line=sep_line)
        print(balance_sentence)

        # ジュースの最低価格とSuicaの残高の比較
        purchasable = is_purchasable(min_price)
        if not purchasable:
            print(f'Suicaの残高が不足しています。最低でも{min_price}円以上の残高が必要です')
            break
        
        # 購入処理
        options = []
        for juice_list in range(zip(vm._juice_lists, vm.stocks)):
            option = f'{juice_list}'
        txt = '購入したいジュースの番号を入力してください > '
        i = view.choose_juice(juice_lists, txt)  # 選択したjuice_listsのindex番号 iを取得
        perchased_juice = vm.stocks[i].pop(0)  # pop()によって在庫は1本減る
        
        # Suicaの残高から支払い
        print(f'購入前のSuicaの残高 {suica.balance}')
        suica.add_balance(-perchased_juice.price)  # ジュースの購入額をSuicaの残高から差し引く
        print(f'購入後のSuicaの残高 {suica.balance}')
        
        # 自動販売機に売上額を計上
        print(f'購入前の自販機の売上金合計 {vm.proceeds}')
        vm.add_proceeds(perchased_juice.price)
        print(f'購入後の自販機の売上金合計 {vm.proceeds}')
        
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


# mode選択
def mode_select(options):
    # view.pyの関数を指定: 画面表示 > 標準入力 >バリデーションチェック > 入力値をリターン
    selected_option = view.get_selected_option(options)
    
    return selected_option


if __name__ == '__main__':
    # 初期設定 -- constants
    DEFAULT_DEPOSIT = 500
    # MIN_DEPOSIT = 100  # 可能なら定数として設定したい  --> エラーのクラスにどのようにして反映させるか
    JUICE_LISTS = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)]
    DEFAULT_NUM = 5
    MODE_OPTIONS = ('Suicaにチャージ', 'ジュースの購入', 'ジュースの補充')

    # 初期設定値 -- 変数
    sep_line = '=' * 60 + '\n'

    # 初期設定 -- 在庫管理用のリストを生成 --> 自動販売機のコンストラクタに組み込んだ
    # stocks = []
    # for i in range(len(JUICE_LISTS)):
    #     created_list = create_juice(i=i, juice_lists=JUICE_LISTS, num=DEFAULT_NUM)
    #     stocks.append(created_list)

    # SuicaとVendingMachineクラスのインスタンス化
    suica = Suica(DEFAULT_DEPOSIT)
    vm = VendingMachine(JUICE_LISTS, DEFAULT_NUM)
    print(f'在庫: {vm.get_stock_nums()}')

    # # ここからメイン処理（whileループ）
    # mode = mode_select(MODE_OPTIONS)

    # # [0]: Suicaにチャージ
    # if mode == '0':
    #     charge_to_suica()

    # # [1]: ジュースの購入
    # if mode == '1':
    #     purchase_juice(i, JUICE_LISTS)


    # # [2]: ジュースの補充
    # if mode == '2':
    #     pass


    # # [q]: ループ処理の終了
    # if mode == 'q':
    #     pass