import random
import nonebot
from nonebot import require

scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job('cron', hour='10,15,20')
async def _():
    bot = nonebot.get_bot()
    qq_map = {
        '2314528974': 'hz',
        '997239275': 'yh',
        '446048635': '诚哥',
        '735463522': 'gw',
        '1014577003': 'fy',
        '997858770': 'yz',
        '1253156026': '小黑',
        '634493876': 'zy',
        '907410314': 'jk'
    }
    p = random.choice(list(qq_map.items()))
    msg = [
        {
            'type': 'at',
            'data': {
                'qq': int(p[0])
            }
        },
        {
            'type': 'text',
            'data': {
                'text': f'{p[1]}还不提肛?!'
            }
        }
    ]
    await bot.send_group_msg(group_id=600302544, message=msg)
