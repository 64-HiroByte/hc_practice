import view

from models import Suica
from models import VendingMachine
from my_exceptions import InsufficientBalanceError
from my_exceptions import NoStockError
from my_exceptions import SmallDepositError


def get_balance_msg(suica):
    """Suicaの残高を表示する文字列の取得

    Args:
        suica (object): Suicaクラスをインスタンス化したオブジェクト

    Returns:
        str: 現在のSuicaの残高を記述したもの
    """    
    return f'現在のSuicaの残高は {suica.balance}円 です\n'


def charge_to_suica(suica, sep_line='', quit='q'):
    """Suicaにチャージ（入金）する処理

    Args:
        suica (object): Suicaクラスをインスタンス化したオブジェクト
        sep_line (str, optional): 仕切り線（初期値 ''）
        quit (str, optional): 前の画面に戻る時に入力するコマンド（初期値 'q'）
    """    
    while True:
        # 現在のSuicaの残高を取得し表示
        view.show_message(sep_line, get_balance_msg(suica))
        
        # 入金額を入力
        input_value = view.input_deposit(suica.min_deposit)
        
        # quit（q）が入力された場合の処理
        if input_value == quit:
            break
        
        # 入金処理とエラーハンドリング
        try:
            suica.add_deposit(input_value)
        except SmallDepositError as e:
            print(e)
            continue
        
        # 入金完了処理
        additional_msg = f'Suicaに {input_value}円 チャージしました\n'
        view.show_message(sep_line, get_balance_msg(suica), additional_msg)
        break


def get_stock_options(suica=None, vm=None, purchase=True):
    """ジュースの名前と価格、ステータスを格納した選択肢を作成

    Args:
        suica (object, optional): Suicaクラスをインスタンス化したオブジェクト（初期値 None）
        vm (object, optional): VendingMachineクラスをインスタンス化したオブジェクト（初期値 None）
        purchase (bool, optional): 購入処理フラグ（初期値 True）

    Returns:
        list: ジュースの名前と価格、ステータス（在庫本数など）を格納したリスト
    """
    juice_lists = vm.juice_lists
    stock_nums = vm.get_stock_nums()
    
    # 選択肢の作成
    stock_options = []
    for i, juice_list, in enumerate(juice_lists):
        status = f': 残り {stock_nums[i]}本'
        
        if purchase:  #　購入の場合
            price = f'（{juice_list[1]}円）'
            if stock_nums[i] == 0:
                status = ': 売り切れ'
            elif juice_list[1] > suica.balance:
                status = ': 残高不足'
        else:  # 補充の場合
            price = ''
        option = f'{juice_list[0]}{price}{status}'
        stock_options.append(option)
    return stock_options


def purchase_juice(suica, vm, sep_line='', quit='q'):
    """ジュースを購入する

    Args:
        suica (object, optional): Suicaクラスをインスタンス化したオブジェクト（初期値 None）
        vm (object, optional): VendingMachineクラスをインスタンス化したオブジェクト（初期値 None）
        sep_line (str, optional): 仕切り線（初期値 ''）
        quit (str, optional): 前の画面に戻る時に入力するコマンド（初期値 'q'）
    """
    juice_lists = vm.juice_lists
    # 自販機で扱うジュースの最低価格を取得
    min_price = min([juice[1] for juice in juice_lists])
    
    while True:
        # 販売可能な商品の有無
        in_stock_num = 0
        for stock in vm.stocks:
            in_stock_num += len(stock)
        if in_stock_num == 0:
            msg = '全商品が売り切れです。補充してください\n'
            view.show_message(sep_line, msg)
            break
        
        # ジュースの最低価格とSuicaの残高の比較
        if min_price > suica.balance:
            # 追加メッセージの設定
            additional_msg = f'Suicaの残高が不足しています。最低でも{min_price}円以上の残高が必要です\n'
        else:
            additional_msg = ''
        
        # Suicaの残高表示
        view.show_message(sep_line, get_balance_msg(suica), additional_msg)
        if additional_msg:
            break
        
        # 購入処理
        stock_options = get_stock_options(suica, vm)
        msg = '購入したいジュースの番号を選択してください\n'
        selected_option = view.input_selected_option(stock_options, msg, sep_line)
        
        if selected_option == quit:
            break
        
        i = int(selected_option)
        # バリデーションチェック （購入商品と残高の比較）
        try:
            vm.is_purchasable(i, suica.balance)
        except InsufficientBalanceError as e:
            print(e)
            continue
        # バリデーションチェック （購入商品の在庫確認）
        try:
            vm.is_in_stock(i)
        except NoStockError as e:
            print(e)
            continue

        # 自動販売機の在庫を1減らし、売上金の加算、Suicaから支払いを実行
        purchased_juice = vm.stocks[i].pop(0)
        amount = purchased_juice.price
        vm.add_proceeds(amount)
        suica.add_deposit(amount, deposit=False)
        
        # 購入処理完了
        purchased_msg = f'{purchased_juice.name}({amount}円)を購入しました。Suicaの残高は{suica.balance}円です'
        view.show_message(sep_line, purchased_msg)
        
        # 反復処理の確認
        res = view.input_yes_or_no('続けて購入しますか？')
        if res == 'n':
            break
        else:
            continue


def restock_juice(vm, sep_line='', quit='q'):
    """自動販売機にジュースを補充する

    Args:
        vm (object, optional): VendingMachineクラスをインスタンス化したオブジェクト
        sep_line (str, optional): 仕切り線（初期値 ''）
        quit (str, optional): 前の画面に戻る時に入力するコマンド（初期値 'q'）
    """
    juice_lists =vm.juice_lists
    msg = [
        '補充するジュースの番号を選択してください',
        f'補充する本数を入力してください（戻る場合は "{quit}" を入力） > ',
        '続けて補充しますか？'
        ]
    
    while True:
        # 在庫状況の取得と選択
        stock_options = get_stock_options(vm=vm, purchase=False)
        selected_option = view.input_selected_option(stock_options, msg[0], sep_line, quit)
        if selected_option == quit:
            break
        
        # 補充するジュースのインデックス番号
        i = int(selected_option)
        
        # 補充する本数の入力
        num = view.input_value_validation(msg[1], quit)
        if num == quit:
            break

        # ジュースの補充
        vm.restock(i, num)
        
        # 補充処理完了
        restocked_msg = f'{juice_lists[i][0]}を{num}本補充しました'
        view.show_message(sep_line, restocked_msg)
        
        # 反復処理の確認
        res = view.input_yes_or_no(msg[2])
        if res == 'n':
                break
        else:
            continue
        
        
def show_statuses(suica, vm, sep_line=''):
    """各種ステータスを表示させる

    Args:
        ssuica (object, optional): Suicaクラスをインスタンス化したオブジェクト
        vm (object, optional): VendingMachineクラスをインスタンス化したオブジェクト
        sep_line (str, optional): 仕切り線（初期値 ''）
    """
    juice_lists = vm.juice_lists
    stock_nums = vm.get_stock_nums()
    proceeds = vm.proceeds
    
    msg_lists = [get_balance_msg(suica), '** 自動販売機の在庫状況 **']
    for juice_list, stock_num in zip(juice_lists, stock_nums):
        msg_list = f'- {juice_list[0]}（{juice_list[1]}円）: 在庫{stock_num}本'
        msg_lists.append(msg_list)
    
    msg_lists.append(f'\n現在の自動販売機の売上金額は {proceeds}円です')
    
    msg = '\n'.join(msg_lists)
    
    view.show_message(sep_line, msg)

# mode選択
def mode_select(options, sep_line):
    """行動を選択する

    Args:
        options (tuple): 行動の選択肢
        sep_line (str, optional): 仕切り線（初期値 ''）

    Returns:
        str: 標準入力によって得た選択肢の番号（文字列）
    """    
    msg = '\n何をしますか？\n'
    selected_option = view.input_selected_option(options, msg, sep_line)
    
    return selected_option


def main():
    DEFAULT_DEPOSIT = 500
    MIN_DEPOSIT = 100
    JUICE_LISTS = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)]
    DEFAULT_NUM = 5
    MODE_OPTIONS = ('Suicaにチャージ', 'ジュースの購入', 'ジュースの補充', 'ステータス表示')

    # 初期設定値 -- 変数
    sep_line = '=' * 70 + '\n'
    suica = Suica(DEFAULT_DEPOSIT, MIN_DEPOSIT)
    vm = VendingMachine(JUICE_LISTS, DEFAULT_NUM)
    
    while True:
        mode = mode_select(MODE_OPTIONS, sep_line)

        if mode == '0':  # Suicaにチャージ
            charge_to_suica(suica, sep_line)
        
        if mode == '1':  # ジュースの購入
            purchase_juice(suica, vm, sep_line)
        
        if mode == '2':  # ジュースの補充
            restock_juice(vm, sep_line)
        
        if mode == '3':  # ジュースの補充
            show_statuses(suica, vm, sep_line)

        if mode == 'q':  # ループ処理の終了
            break
