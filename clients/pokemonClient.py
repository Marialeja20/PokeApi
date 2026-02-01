import httpx
from fastapi import HTTPException
from appsettings import AppSettings

class PokemonClient:
    def __init__(self):
        # Usamos la URL definida en appsettings
        self.base_url = AppSettings.POKEAPI_URL

    async def get_pokemon_data(self, pokemon_name: str, http_client: httpx.AsyncClient) -> dict:
        url = f"{self.base_url}{pokemon_name}"
        
        try:
            response = await http_client.get(url, timeout=AppSettings.TIMEOUT_SECONDS)
            
            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail=f"Pokémon '{pokemon_name}' no encontrado."
                )
            
            response.raise_for_status()
            return response.json()
            
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Error de conexión con PokeAPI")