class SmallDepositError(Exception):
    def __str__(self):
        return 'SmallDepositError: 100円未満のチャージはできません'


class InsufficientBalanceError(Exception):
    def __str__(self):
        return 'InsufficientBalanceError: 残高が不足しているので購入できません'