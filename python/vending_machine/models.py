class SmallDepositError(Exception):
    def __str__(self):
        return print('SmallDepositError: 100円未満のチャージはできません')

class Suica(object):
    def __init__(self, deposit):
        self._balance = deposit 
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        try:
            if amount >= 100:
                self._balance += amount
            else:
                raise SmallDepositError
        except SmallDepositError as e:
            print(e)


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
        
        self._stocks = []
        for i in range(len(juice_lists)):
            created_list = self.create_juice(i, self._juice_lists, default_num)
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
    def proceeds(self):
        return self.__proceeds  # 自販機の売上金額の取得
    
    def add_proceeds(self, price):
        self.__proceeds += price  # 自販機の売上金額に商品代金を加算
    
    # 改善の余地あり
    @property
    def stocks(self):
        return self._stocks  # 自販機の在庫情報の取得
    
    @stocks.setter
    def stocks(self, name, quantity):
        
        self._stocks[name] += quantity  # 自販機の在庫の加減算
    
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

