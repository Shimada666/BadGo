import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from fastapi import APIRouter
from nonebot.plugin import get_loaded_plugins, Plugin
from superstream import Stream

from src.util.web_response import WebResponse

router = APIRouter()


@dataclass
class PluginBO:
    class Meta:
        name: str
        description: str

    meta: Meta


@router.get('/plugins')
def index():
    plugins = get_loaded_plugins()

    def _plugin_to_dict(plugin: Plugin):
        return {
            "name": plugin.name,
            "module": plugin.module.__file__,
            "matcher": len(plugin.matcher)
        }

    data = (Stream(plugins)
            .map(_plugin_to_dict)
            .to_list())

    return WebResponse.build_data(data)
    # def read_yaml(filepath: str) -> dict:
    #     with open(filepath, 'r', encoding='utf8') as f:
    #         return yaml.load(f.read(), Loader=yaml.SafeLoader)
    #
    # p = Path('src/plugins')
    # plugins = (Stream(p.iterdir())
    #            .filter(lambda x: x.is_dir())
    #            .map(lambda x: read_yaml(os.path.join(str(x), 'config.yml')))
    #            .to_list())
    # return plugins
