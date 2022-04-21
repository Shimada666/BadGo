import random
import typing

from nonebot import on_regex
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State


def create_matcher(pattern: str, response: typing.List[str], probability=0.7):
    le = on_regex(pattern)

    @le.handle()
    async def _(bot: Bot, event: Event, state: T_State):
        if random.random() < probability:
            msg = random.choice(response)
            await le.send(msg)


test = [
    {
        "pattern": "人权",
        "response": ["美国就是全球最大人权赤字国！", "美国人权劣迹罄竹难书！"],
        "probability": 0.7
    },
    {
        "pattern": "言论自由",
        "response": ["新闻自由在美国就是个笑话！", "在中国，任何人都不可能因言获罪！"],
        "probability": 0.5
    },
    {
        "pattern": "疫情|清零|共存|新冠|解封",
        "response": ["中国应对疫情比美国胜强百倍！", "在座各位疫情期间生活在中国，就偷着乐吧！", "上海的疫情与美国相比微不足道！", "中国疫苗外交广受欢迎！"],
        "probability": 0.5
    },
    {
        "pattern": "美国|中国",
        "response": ["美国这种行为，无疑是搬起石头砸自己的脚！", "责任全在美方！", "美方不要反复拿中国说事儿！"],
        "probability": 0.6
    },
    {
        "pattern": "政府|上海",
        "response": ["责任全在美方！", "在座各位疫情期间生活在中国，就偷着乐吧！"],
        "probability": 0.7
    }
]

for i in test:
    create_matcher(i["pattern"], i["response"], i.get('probability', 0.7))
