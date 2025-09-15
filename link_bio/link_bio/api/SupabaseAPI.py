import os
import dotenv
from supabase import create_client, Client
from link_bio.model.Featured import Featured

class SupabaseAPI:
    def __init__(self) -> None:
        # Cargar variables de entorno
        dotenv.load_dotenv()
        self.SUPABASE_URL: str = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

        if not self.SUPABASE_URL or not self.SUPABASE_KEY:
            raise ValueError("Faltan SUPABASE_URL o SUPABASE_KEY en .env")

        # Crear cliente de supabase
        self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def featured(self) -> list[Featured]:
        response = self.supabase.table("featured").select("*").execute()

        featured_data = []
        if response.data:
            for featured_item in response.data:
                featured_data.append(
                    Featured(
                        title=featured_item["title"],
                        image=featured_item["image"],
                        url=featured_item["url"],
                    )
                )
        return featured_data