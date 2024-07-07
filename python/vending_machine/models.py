from my_exceptions import InsufficientBalanceError
from my_exceptions import NoStockError
from my_exceptions import SmallDepositError
    
class Suica(object):
    """Suicaクラス

    Attributes:
        balance (int): Suicaの残高
        min_deposit(int): Suicaへの最少入金額
    Methods:
        add_deposit: 任意の金額を残高に加減算する
    """    
    def __init__(self, default_deposit, min_deposit):
        self.__balance = default_deposit
        self.__min_deposit = min_deposit
    
    @property
    def min_deposit(self):
        return self.__min_deposit
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        """balanceのセッター
        名前修飾してあるため、クラス外で残高を直接変更することを許可していない
        クラス外での属性値の変更に対して例外を発生させる
        Args:
            new_balance (any): ダミーの引数

        Raises:
            AttributeError: クラス外で属性値の変更を行うことで発生
        """
        raise AttributeError('残高を直接変更することは許可されていません。Suicaクラスのメソッドを使用して残高を更新してください')
    
    def add_deposit(self, amount, deposit=True):
        """Suicaの残高を加減算する

        Args:
            amount (int): 加減算する金額
            deposit (bool, optional): 入金処理のフラグ（デフォルトはTrue）

        Raises:
            SmallDepositError: 最少入金額未満の入金を行った場合に発生
            InsufficientBalanceError: 残高不足により支払い出来ない場合に発生
        """
        # 入金
        if deposit:
            if amount >= self.__min_deposit:
                self.__balance += amount
            else:
                raise SmallDepositError
        # 支払い
        else:
            if self.__balance >= amount:
                self.__balance -= amount
            else:  # 出金操作を想定している
                raise InsufficientBalanceError


class Juice(object):
    """Juiceクラス

    Attributes:
        name (str): ジュースの名前
        price (int): ジュースの販売価格
    """    
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price


class VendingMachine(object):
    """自動販売機クラス

    Attributes:
        proceeds (int): 自動販売機の売上金
        juice_lists(list): ジュースの名前と価格のタプルのリスト
        stocks(list): 自動販売機に格納されているジュースオブジェクトを格納したリスト

    Methods:
        create_juice: ジュースを生成
        add_proceeds: 売上金の加算
        restock: ジュースの補充
        get_stock:nums: 在庫本数の取得
        is_purchasable: ジュースの値段とSuica残高の比較
        is_in_stock: ジュースの在庫確認

    Raises:
        AttributeError: クラス外で属性値の変更を行うことで発生
        InsufficientBalanceError: 残高が不足している場合に発生
        NoStockError: 
    """    
    # 在庫と売上金の初期設た
    def __init__(self, juice_lists, default_num):
        self.__proceeds = 0
        self._juice_lists = juice_lists
        # 初期在庫のジュースの生成
        self._stocks = []
        for i in range(len(juice_lists)):
            created_list = self.create_juice(i, default_num)
            self._stocks.append(created_list)

    def create_juice(self, i, num):
        """選択したジュースを任意の本数インスタンス化する

        Args:
            i (int): juice_listsのインデックス番号
            num (int): 生成するジュースの本数
        
        Returns:
            list: 生成したジュースオブジェクトを格納したリスト
        """
        juice_lists = self._juice_lists
        created_juice = [Juice(name=juice_lists[i][0], price=juice_lists[i][1]) for _ in range(num)]
        
        return created_juice
    
    @property
    def juice_lists(self):
        return self._juice_lists
    
    @property
    def proceeds(self):
        return self.__proceeds
    
    @proceeds.setter
    def proceeds(self, amount):
        """proceedsのセッター
        名前修飾してあるため、クラス外で残高を直接変更することを許可していない
        クラス外での属性値の変更に対して例外を発生させる
        Args:
            amount (any): ダミーの引数

        Raises:
            AttributeError: クラス外で属性値の変更を行うことで発生
        """
        raise AttributeError('売上金を直接変更することは許可されていません。\
            VendingMachineクラスのメソッドを使用して売上金を更新してください')
    
    def add_proceeds(self, amount):
        self.__proceeds += amount
    
    @property
    def stocks(self):
        return self._stocks
    
    def restock(self, i, num):
        """選択したジュースを任意の本数補充する

        Args:
            i (int): juice_listsのインデックス番号
            num (int): 生成するジュースの本数
        """
        created_juice = self.create_juice(i, num)
        self._stocks[i].extend(created_juice)
    
    def get_stock_nums(self):
        """ジュースオブジェクトの数から在庫本数のリストを取得

        Returns:
            list: ジュースの在庫本数(int）
        """
        stock_nums = []
        for i in range(len(self._stocks)):
            stock_num = len(self._stocks[i])
            stock_nums.append(stock_num)
        return stock_nums
    
    def is_purchasable(self, i, balance):
        """ジュースの値段とSuica残高の比較

        Args:
            i (int): juice_listsのインデックス番号
            balance (int): Suicaの残高

        Raises:
            InsufficientBalanceError: 残高不足により支払い出来ない場合に発生
        """
        if self._juice_lists[i][1] > balance:
            raise InsufficientBalanceError
    
    def is_in_stock(self, i):
        """在庫の確認

        Args:
            i (int): 在庫のリスト（stocks)のインデックス番号

        Raises:
            NoStockError: 売り切れの商品を購入しようとした場合に発生
        """
        if self._stocks[i] == []:
            raise NoStockError
