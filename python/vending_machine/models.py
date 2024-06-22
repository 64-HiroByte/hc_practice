class Suica(object):
    '''
    - 100円以上の任意の金額をチャージできる
    - 100円未満はチャージできない（例外を発生する）
    - 残高を取得できる
    '''
    id = 0
    
    def __init__(self, deposit):
        self.__deposit = deposit  # depositは名前修飾する?
        self.id = Suica.id
        Suica.id += 1
    
    @property
    def deposit(self):
        return self.__deposit
    
    @deposit.setter
    def deposit(self, amount):
        if amount >= 100:
            self.__deposit += amount  # 支払いの場合は-amount


class Juice(object):
    '''
    - 名前と値段の情報を持つ
    '''
    
    def __init__(self, name, price_dict):
        self.name = name
        self.price = price_dict[name]


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
    def __init__(self, default_stock):
        self._stock_dict = default_stock
        self.__proceed = 0
    
    @property
    def proceed(self):
        return self.__proceed  # 自販機の売上金額の取得
    
    @proceed.setter
    def deposit(self, price):
        self.__proceed += price  # 自販機の売上金額に商品代金を加算
    
    @property
    def stock_dict(self):
        return self._stock_dict  # 自販機の在庫情報の取得
    
    @stock_dict.setter
    def stock_dict(self, name, quantity):
        self._stock_dict[name] += quantity  # 自販機の在庫の加減算
    
    # 購入処理
    # def purchase_beverage(self, juice):
    #     pass
    
    # # 商品補充
    # def refill_beverage(self, juice, quantity):
    #     pass
    
# 商品の初期在庫
default_stock = {'ペプシ': 5, }  # [TODO] 機能拡張で全商品の在庫を５にする


    # vending_machine = VendingMachine(default_stock)
    # vending_machine.stock_dict['いろはす'] = 5
    # print(vending_machine.stock_dict)
    
vm = VendingMachine(default_stock=default_stock)
vm.stock_dict['ペプシ'] += -1  # 購入による在庫の減算
print(vm.stock_dict)