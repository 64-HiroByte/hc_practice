class SmallDepositError(Exception):
    def __str__(self):
        return '\nSmallDepositError: 100円未満のチャージはできません\n'


class InsufficientBalanceError(Exception):
    def __str__(self):
        return '\nInsufficientBalanceError: 残高が不足しているので購入できません\n'

        
class NoStockError(Exception):
    def __str__(self):
        return '\nNoStockError: 売り切れのため購入できません\n'