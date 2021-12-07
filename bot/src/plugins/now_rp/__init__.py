import math
import random

import httpx
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from src.common.util.message import MessageUtil

matcher = on_command("nowrp")


def get_legal_rp() -> int:
    anu_api_url = f'https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8'
    resp = httpx.get(anu_api_url)
    seed = resp.json()['data'][0]
    random.seed(seed)
    x = random.normalvariate(50, 50)
    if x > 100 or x < 0:
        return get_legal_rp()
    else:
        return round(x)


@matcher.handle()
async def now_rp(bot: Bot, event: Event, state: T_State):
    sender = int(event.get_user_id())
    msg = []
    msg.append(MessageUtil.new_at(sender))
    try:
        x = get_legal_rp()
        msg.append(MessageUtil.new_text_msg(f'(当前人品版)你当前的人品是 {x}%'))
    except Exception as e:
        msg.append(MessageUtil.new_text_msg(str(e)))
    await matcher.send(msg)
