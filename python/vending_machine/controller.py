import view

from models import Suica
from models import VendingMachine
from my_exceptions import InsufficientBalanceError
from my_exceptions import NoStockError
from my_exceptions import SmallDepositError


def get_balance_msg():
    return f'現在のSuicaの残高は {suica.balance}円 です\n'


def charge_to_suica(sep_line='', quit='q'):
    while True:
        # 現在のSuicaの残高を取得
        view.show_message(sep_line, get_balance_msg())
        
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
        
        additional_msg = f'Suicaに {input_value}円 チャージしました\n'
        view.show_message(sep_line, get_balance_msg(), additional_msg)
        break


def get_stock_options(juice_lists, stock_nums, purchase=True):
    stock_options = []
    for i, juice_list, in enumerate(juice_lists):
        status = f'残り {stock_nums[i]}本'
        
        if purchase:
            price = f'（{juice_list[1]}円）'
            if stock_nums[i] == 0:
                status = '売り切れ'
            elif juice_list[1] > suica.balance:
                status = '残高不足'
        else:
            price = ''
        option = f'{juice_list[0]}{price}    {status}'
        stock_options.append(option)
    return stock_options


# ジュースの購入操作
def purchase_juice(juice_lists, sep_line='', quit='q'):
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
        
        # Suica残高表示
        view.show_message(sep_line, get_balance_msg(), additional_msg)
        if additional_msg:
            break
        
        # 購入処理
        stock_options = get_stock_options(vm.juice_lists, vm.get_stock_nums())
        msg = '購入したいジュースの番号を選択してください\n'
        selected_option = view.get_selected_option(stock_options, msg, sep_line)
        
        if selected_option == quit:
            break
        
        i = int(selected_option)
        # 購入商品と残高の比較
        try:
            vm.is_purchasable(i, suica.balance)
        except InsufficientBalanceError as e:
            print(e)
            continue
        # 購入商品の在庫確認
        try:
            vm.is_in_stock(i)
        except NoStockError as e:
            print(e)
            continue
        
        purchased_juice = vm.stocks[i].pop(0)
        amount = purchased_juice.price
        vm.add_proceeds(amount)
        suica.add_deposit(amount, deposit=False)
        
        purchased_msg = f'{purchased_juice.name}({amount}円)を購入しました。Suicaの残高は{suica.balance}円です'
        view.show_message(sep_line, purchased_msg)
        txt = '続けて購入しますか？'
        res = view.input_yes_or_no(txt)
        if res == 'n':
            break
        else:
            continue


# ジュースの補充: whileループ
def restock_juice(juice_lists, sep_line='', quit='q'):
    msg = [
        '補充するジュースの番号を選択してください',
        f'補充する本数を入力してください（戻る場合は "{quit}" を入力） > ',
        '続けて補充しますか？'
        ]
    
    while True:
    # 在庫状況の取得
        stock_options = get_stock_options(juice_lists, vm.get_stock_nums(), purchase=False)
        selected_option = view.get_selected_option(stock_options, msg[0], sep_line, quit)
        if selected_option == quit:
            break
        else:
            i = int(selected_option)
        num = view.input_value_validation(msg[1], quit)
        if num == quit:
            break
        vm.restock(i, num)
        restocked_msg = f'{juice_lists[i][0]}を{num}本補充しました'
        view.show_message(sep_line, restocked_msg)
        res = view.input_yes_or_no(msg[2])
        if res == 'n':
                break
        else:
            continue 

# mode選択
def mode_select(options, sep_line):
    msg = '何をしますか？'
    selected_option = view.get_selected_option(options, msg, sep_line)
    
    return selected_option


def main():
    while True:
        juice_lists = vm.juice_lists
        mode = mode_select(MODE_OPTIONS, sep_line)

        # [0]: Suicaにチャージ
        if mode == '0':
            charge_to_suica(sep_line)
        # [1]: ジュースの購入
        if mode == '1':
            purchase_juice(juice_lists, sep_line)
        # [2]: ジュースの補充
        if mode == '2':
            restock_juice(juice_lists, sep_line)
        # [q]: ループ処理の終了
        if mode == 'q':
            break


if __name__ == '__main__':
    DEFAULT_DEPOSIT = 500
    MIN_DEPOSIT = 100
    JUICE_LISTS = [('ペプシ', 150), ('モンスター', 230), ('いろはす', 120)]
    DEFAULT_NUM = 1
    MODE_OPTIONS = ('Suicaにチャージ', 'ジュースの購入', 'ジュースの補充')

    # 初期設定値 -- 変数
    sep_line = '=' * 70 + '\n'
    suica = Suica(DEFAULT_DEPOSIT, MIN_DEPOSIT)
    vm = VendingMachine(JUICE_LISTS, DEFAULT_NUM)
    main()