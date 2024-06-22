from models import Juice
from models import Suica
from models import VendingMachine


def generate_suica(deposit=500):
    suica = Suica(deposit)
    return suica

def charge_to_suica(amount):
    if amount >= 100:
        suica.deposit = amount
    else:
        print('[exeption] 100円未満のチャージはできません')


suica = generate_suica()

charge_to_suica(900)
print(f'Suicaの残高: {suica.deposit}円')

