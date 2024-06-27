class Suica(object):
    '''
    - 100円以上の任意の金額をチャージできる
    - 100円未満はチャージできない（例外を発生する）
    - 残高を取得できる
    '''
    def __init__(self, deposit):
        self.__balance = deposit 
    
    def add_balance(self, amount):
        self.__balance += amount  # 支払いの場合は-amount
    
    def show_balance(self):
        return self.__balance


class Juice(object):
    '''
    - 名前と値段の情報を持つ
    '''
    
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine(object):
    '''
    - 在庫を取得できる
    - 購入できるか判定することができる
    - 購入操作で行うこと
        - 購入したジュースの在庫を減らす
        - 売上金額にジュースの値段を加える
        - Suicaのチャージ残高を減らす
    - 購入操作の例外
        - Suicaの残高が不足
        - 在庫のないジュースを購入したとき
    - 購入可能なジュースのリストを取得できる
    - ジュースを補充できる
    '''
    
    # 在庫と売上金の初期設定
    def __init__(self, inventory):
        self._inventory = inventory
        self.__proceeds = 0
    
    def show_proceeds(self):
        return self.__proceeds  # 自販機の売上金額の取得
    
    def add_proceeds(self, price):
        self.__proceeds += price  # 自販機の売上金額に商品代金を加算
    
    @property
    def stocks(self):
        return self._inventory  # 自販機の在庫情報の取得
    
    @stocks.setter
    def stocks(self, name, quantity):
        self._inventory[name] += quantity  # 自販機の在庫の加減算
    
    # 購入処理
    # def purchase_beverage(self, juice):
    #     pass
    
    # # 商品補充
    # def refill_beverage(self, juice, quantity):
    #     pass
    


    # vending_machine = VendingMachine(default_stock)
    # vending_machine.stock_dict['いろはす'] = 5
    # print(vending_machine.stock_dict)
    
# vm = VendingMachine(default_stock=default_stock)
# vm.stock_dict['ペプシ'] += -1  # 購入による在庫の減算
# print(vm.stock_dict)
