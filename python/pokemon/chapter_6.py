import abc


# Pokemonクラスを抽象クラスとする --> 継承する前提なのでインスタンス化できない
class Pokemon(metaclass=abc.ABCMeta):
    def __init__(self, name, type1, type2, hp):
        self.__name = name  # name属性を名前修飾
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    @abc.abstractmethod  # このデコレータをつけたメソッドは継承先でオーバーライド必須(interfaceのようなもの)
    def attack(self):
        print(f'{self.__name} のこうげき')
    
    @abc.abstractmethod  # このデコレータをつけたメソッドは継承先でオーバーライド必須(interfaceのようなもの)
    def change_name(self, new_name):
        if new_name == 'うんこ':
            print('不適切な名前です')
        else:
            self.__name = new_name
    
    @property
    def name(self):
        return self.__name
    
    # name属性に直接アクセスしても何もしない
    @name.setter
    def name(self, new_name):
        pass



# Pokemonクラス（抽象クラス）を継承したSubクラス
class Pikachu(Pokemon):
    # ｓｕｐｅｒクラスのメソッドのオーバーライド
    def attack(self):
        super().attack()  # superクラスのattackメソッドの実行
        print(f'{self.name} の10万ボルト!')  # subクラスで追加する内容
    
    def change_name(self, new_name):
        return super().change_name(new_name)


# サブクラス（Pikachu）のインスタンス化
pika = Pikachu(name='ピカチュウ', type1='でんき', type2='', hp=100)
print(pika.name)
pika.attack()
pika.change_name('うんこ')
print(pika.name)
pika.name = 'This is your new name'  # name属性に直接書き込み
print(pika.name)  # 
