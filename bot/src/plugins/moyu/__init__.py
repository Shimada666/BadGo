from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from src.common.util.message import MessageUtil

matcher = on_command("moyu")


@matcher.handle()
async def moyu(bot: Bot, event: Event, state: T_State):
    msg = []
    msg.append(MessageUtil.new_text_msg(f'http://moyu.corgi.plus 一起来摸鱼吧'))
    await matcher.send(msg)
