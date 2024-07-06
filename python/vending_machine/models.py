from my_exceptions import InsufficientBalanceError
from my_exceptions import NoStockError
from my_exceptions import SmallDepositError
    
class Suica(object):
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
        raise AttributeError('残高を直接変更することは許可されていません。Suicaクラスのメソッドを使用して残高を更新してください')
    
    def add_deposit(self, amount, deposit=True):
        if deposit:
            if amount >= self.__min_deposit:
                self.__balance += amount
            else:
                raise SmallDepositError
        else:
            if self.__balance >= amount:
                self.__balance -= amount
            else:  # 出金操作を想定している
                raise InsufficientBalanceError


class Juice(object):
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
    # 在庫と売上金の初期設定
    def __init__(self, juice_lists, default_num):
        self.__proceeds = 0
        self._juice_lists = juice_lists
        
        # リスト内包表記にするか検討する
        self._stocks = []
        for i in range(len(juice_lists)):
            created_list = self.create_juice(i, juice_lists, default_num)
            self._stocks.append(created_list)

    def create_juice(self, i, juice_lists, num):
        """
        juice_listsに格納されているジュースを選択して任意の本数インスタンス化する関数

        Args:
            i (int): juice_listsを表示して、標準入力された値（インデックス番号）
            juice_lists (list): 使用可能なジュースの名前と値段のlist
            num (int): 生成するジュースの本数
        """
        created_juice = [Juice(name=juice_lists[i][0], price=juice_lists[i][1]) for _ in range(num)]
        
        return created_juice
    
    @property
    def juice_lists(self):
        return self._juice_lists
    
    @property
    def proceeds(self):
        return self.__proceeds  # 自販機の売上金額の取得
    
    @proceeds.setter
    def proceeds(self, amount):
        raise AttributeError('売上金を直接変更することは許可されていません。VendingMachineクラスのメソッドを使用してu売上金を更新してください')
    
    def add_proceeds(self, amount):
        self.__proceeds += amount  # 自販機の売上金額に商品代金を加算
    
    @property
    def stocks(self):
        return self._stocks  # 自販機の在庫情報の取得
    
    def restock(self, i, num):
        created_juice = self.create_juice(i, self._juice_lists, num)
        self._stocks[i].extend(created_juice)
    
    def get_stock_nums(self):
        """
        juice_listsと自動販売機に格納されているジュースオブジェクトの数から在庫本数を取得する関数
        Args:
            juice_lists (list): ジュースの名前と値段の組み合わせ（tuple）を格納したリスト
        Returns:
            list: ジュースの名前[0]と在庫本数[1]のリストを格納した2次元リスト
        """
        stock_nums = []
        for i in range(len(self._juice_lists)):
            stock_num = [self._juice_lists[i][0], len(self._stocks[i])]
            stock_nums.append(stock_num)
        return stock_nums
    
    def is_purchasable(self, i, balance):
        if self._juice_lists[i][1] > balance:
            raise InsufficientBalanceError
    
    def is_in_stock(self, i):
        if self._stocks[i] == []:
            raise NoStockError

