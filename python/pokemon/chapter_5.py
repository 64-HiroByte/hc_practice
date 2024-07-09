import abc


# Pokemonクラスを抽象クラスとする --> 継承する前提なのでインスタンス化できない
class Pokemon(metaclass=abc.ABCMeta):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    @abc.abstractmethod # このデコレータをつけたメソッドは継承先でオーバーライド必須(interfaceのようなもの)
    def attack(self):
        print(f'{self.name} のこうげき')


class Pikachu(Pokemon):
    # ｓｕｐｅｒクラスのメソッドのオーバーライド
    def attack(self):
        super().attack()  # superクラスのattackメソッドの実行
        print(f'{self.name} の10万ボルト!')  # subクラスで追加する内容


'''
抽象クラス（Pokemonクラス）をインスタンス化しようとすると、次のエラーが発生する
TypeError: Can't instantiate abstract class Pokemon with abstract method attack
'''
# poke = Pokemon(name='リザードン', type1='ほのお', type2='ひこう', hp=100)
# print(poke.name)
# print(poke.type1)
# poke.attack()

# サブクラス（Pikachu）のインスタンス化
pika = Pikachu(name='ピカチュウ', type1='でんき', type2='', hp=100)
print(pika.name)
pika.attack()


