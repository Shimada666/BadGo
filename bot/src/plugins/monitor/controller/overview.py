import os

from fastapi import APIRouter

from src.util.web_response import WebResponse

router = APIRouter()


@router.get('/info')
def info():
    cwd = os.getcwd()
    return WebResponse.build_data({"name": os.path.basename(cwd), "dir": cwd})
