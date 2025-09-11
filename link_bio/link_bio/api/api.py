import link_bio.constants as c
from starlette.requests import Request
from fastapi import FastAPI
from .SupabaseAPI import SupabaseAPI


fastapi_app = FastAPI()
SUPABASE_API = SupabaseAPI()


async def feactured() -> list:
    return SUPABASE_API.feactured()