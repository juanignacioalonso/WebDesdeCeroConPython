import link_bio.constants as c
from starlette.requests import Request
from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/repo")
async def repo() -> str:
    return c.GIT_URL_CABECERA

@fastapi_app.get("/live/{user}")
async def live(user: str) -> str:
    if user == "mouredev":
        return True
    return False