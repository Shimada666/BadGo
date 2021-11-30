import enum

from src.common.enums import EnumIns


class TradingType(EnumIns, enum.Enum):
    RP = EnumIns(code=0, description='人品插件')
    BLACKJACK = EnumIns(code=1, description='21点')


print(TradingType.RP.code)
