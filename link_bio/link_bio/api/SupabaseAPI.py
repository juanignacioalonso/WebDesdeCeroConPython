import os
import dotenv 


from supabase import create_client, Client

class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
        

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def feactured(self) -> list:

        response = self.supabase.table("feactured").select("*").execute()

        feactured_data = []

        if len(response.data) >0:
            for featured_item in response.data:
                feactured_data.append(featured_item)

        print(feactured_data)

        return feactured_data