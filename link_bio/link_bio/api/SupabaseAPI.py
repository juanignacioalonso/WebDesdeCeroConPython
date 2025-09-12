import os
import dotenv
from supabase import create_client, Client
from link_bio.model.Featured import Featured

class SupabaseAPI:
    dotenv.load_dotenv()
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")


    supabase: Client

    def __init__(self) -> None:
    self.supabase = None

    def create_client(self):
        if self.supabase is None:
            self.supabase = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def featured(self) -> list:

        if self.supabase is None:
            self.create_client()

        response = self.supabase.table("featured").select("*").execute()

        feactured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                feactured_data.append(featured_item)

        return feactured_data