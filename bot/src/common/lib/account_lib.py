from src.common.model import *


class AccountLib:
    @staticmethod
    def get_or_create(qq: int, amount: int = 100) -> (Account, bool):
        return Account.get_or_create(qq=qq, amount=amount)

    @staticmethod
    def get_by_qq(qq: int) -> Account:
        return Account.select().where(Account.qq == qq).first()
