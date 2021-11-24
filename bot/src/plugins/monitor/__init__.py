from nonebot import get_driver
from nonebot.drivers.fastapi import Driver
from .controller import plugin_manager, index, overview

driver: Driver = get_driver()
app = driver.server_app

ROUTE_PREFIX = '/monitor/api/v1'

app.include_router(index.router)
app.include_router(plugin_manager.router, prefix=ROUTE_PREFIX)
app.include_router(overview.router, prefix=ROUTE_PREFIX)
