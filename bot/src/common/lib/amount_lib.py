from peewee import ModelSelect

from src.common.enums.trading_type import TradingType
from src.common.model import *


class AmountLib:
    @staticmethod
    def top_up(type: TradingType, qq: int, amount: int):
        TradingRecord.create(qq=qq, trading_type=type.code, amount=amount)


