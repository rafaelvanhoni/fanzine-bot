
from dotenv import load_dotenv
import requests
import os
from app.core.models.artist import Artist
from app.services.exceptions import DiscogsError

load_dotenv()

class DiscogsService:

    def __init__(self):
        self.__base_url = os.getenv("DISCOGS_URL")
        self.__token = os.getenv("DISCOGS_TOKEN")
        self.__user_agent = os.getenv("USER_AGENT")

    def fetch_data(self, query: str, type: str, per_page: int = 3, page: int = 1):
        url = f"{self.__base_url}/database/search?q={query}&type={type}&per_page={per_page}&page={page}"

        headers = {
            "Authorization": f"Discogs token={self.__token}",
            "User-Agent": self.__user_agent
        }
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise DiscogsError("❌ Erro 401 - Token inválido ou ausente.")
            elif response.status_code == 404:    
                raise DiscogsError("❌ Erro 404 - Recurso não encontrado.")
            elif response.status_code == 429:
                raise DiscogsError("⚠️ Erro 429 - Muitas requisições. Aguarde um pouco e tente novamente.")
            elif 500 <= response.status_code < 600:
                raise DiscogsError(f"⚠️ Erro {response.status_code} - Problema no servidor Discogs.")
            else:
                raise DiscogsError(f"⚠️ Erro inesperado: {response.status_code} - {response.reason}")
        except Exception as e:
            raise DiscogsError("❌ Não foi possível conectar ao Discogs. Verifique sua internet ou tente novamente mais tarde.")