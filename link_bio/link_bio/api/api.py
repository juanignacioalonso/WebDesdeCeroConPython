import link_bio.constants as c
from starlette.requests import Request
from fastapi import FastAPI
from .SupabaseAPI import SupabaseAPI
from link_bio.model.Featured import Featured


fastapi_app = FastAPI()
SUPABASE_API = SupabaseAPI()


async def featured() -> list[Featured]:
    return SUPABASE_API.featured()