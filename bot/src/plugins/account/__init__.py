from nonebot import on_command, CommandGroup
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

from src.common.lib.account_lib import AccountLib
from src.common.util.message import MessageUtil

g = CommandGroup('account')


def h(x):
    return x.handle()


@h(g.command('register', aliases={'注册'}))
async def _(bot: Bot, event: Event, state: T_State):
    sender = int(event.get_user_id())
    account, created = AccountLib.get_or_create(qq=sender)
    to_msg = []
    to_msg.append(MessageUtil.new_at(sender))
    if created:
        to_msg.append(MessageUtil.new_text_msg('注册成功，获得初始资金 100'))
    else:
        to_msg.append(MessageUtil.new_text_msg('已经注册过了'))
    await bot.send(event=event, message=to_msg)


@h(g.command('money', aliases={'余额'}))
async def _(bot: Bot, event: Event, state: T_State):
    sender = int(event.get_user_id())
    account = AccountLib.get_by_qq(qq=sender)
    to_msg = []
    to_msg.append(MessageUtil.new_at(sender))
    if account:
        to_msg.append(MessageUtil.new_text_msg(f'当前余额为: {account.amount}'))
    else:
        to_msg.append(MessageUtil.new_text_msg('您还没有注册！请输入 /account.register 注册'))
    await bot.send(event=event, message=to_msg)
