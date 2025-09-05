import link_bio.constants as c



async def repo() -> str:
    return c.GIT_URL_CABECERA

async def live(user: str) -> str:
    if user == "mouredev":
        return True
    return False