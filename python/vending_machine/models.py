class Suica(object):
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
            self.__deposit += amount
        elif amount >= 0:
            print('[exeption] 100円未満のチャージはできません')
        else:
            self.__deposit += amount
            print(f'{amount}支払い')


class Juice(object):
    
    def __init__(self, name, price_dict):
        self.name = name
        self.price = price_dict[name]


class VendingMachine(object):
    
    # 在庫と売上金の初期設定
    def __init__(self, default_stock):
        self.stock_dict = default_stock
        self.proceed = 0
    
    # 在庫表示
    def stock(self):
        pass
    
    # 購入処理
    def purchase(self, juice, quantity, proceed):
        pass
    
    # 商品補充
    def refill(self, juice, quantity, stock_dict):
        pass
    
    

DEFAULT_AMOUNT = 500
PRICE_DICT = {'ペプシ': 150, 'いろはす': 120, 'モンスター': 230}
# 商品の初期在庫
default_stock = {'ペプシ': 5, }  # [TODO] 機能拡張で全商品の在庫を５にする


suica = Suica(deposit=DEFAULT_AMOUNT)
# suica.deposit = -100
# print(suica.deposit)

vending_machine = VendingMachine(default_stock)
vending_machine.stock_dict['いろはす'] = 5
print(vending_machine.stock_dict)


# suica.charge(150)
# print(suica.get_deposit())
# product = 'ペプシ'
# print(PRICE_DICT[product])