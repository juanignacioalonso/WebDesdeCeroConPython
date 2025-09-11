import os
import dotenv
from supabase import create_client, Client


class SupabaseAPI:
    def __init__(self):
        # Cargar variables de entorno desde .env si existe
        dotenv.load_dotenv()

        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")

        if not supabase_url or not supabase_key:
            raise ValueError("SUPABASE_URL y SUPABASE_KEY son requeridos")

        self.supabase: Client = create_client(supabase_url, supabase_key)

    def featured(self) -> list:
        response = self.supabase.table("feactured").select("*").execute()

        featured_data = []
        if response.data:
            for item in response.data:
                featured_data.append(item)

        return featured_data