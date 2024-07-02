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
                self._balance += amount  # 支払いの場合は-amount
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
    def __init__(self, stocks):
        self._stocks = stocks
        self.__proceeds = 0
        # 取り扱うジュースのリストを追加するか検討
    
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
