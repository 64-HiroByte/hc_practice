class Pokemon(object):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    def attack(self):
        print(f'{self.name} のこうげき')
        
    # def __del__(self):
    #     print('デストラクタが呼び出されました')


class Pikachu(Pokemon):
    # ｓｕｐｅｒクラスのメソッドのオーバーライド
    def attack(self):
        super().attack()  # superクラスのattackメソッドの実行
        print(f'{self.name} の10万ボルト!')  # subクラスで追加する内容



poke = Pokemon(name='リザードン', type1='ほのお', type2='ひこう', hp=100)
print(poke.name)
print(poke.type1)
poke.attack()

# del poke  # デストラクタによるインスタンスの破棄

# サブクラス（Pikachu）のインスタンス化
pika = Pikachu(name='ピカチュウ', type1='でんき', type2='', hp=100)
print(pika.name)
pika.attack()
