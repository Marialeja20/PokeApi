import httpx
from fastapi import HTTPException
from clients.pokemonClient import PokemonClient
# Importante: 'DTOs' debe coincidir con el nombre de tu carpeta
from DTOs.pokemonDtos import PokemonResponseDTO

class PokemonService:
    def __init__(self):
        self.client = PokemonClient()

    async def get_pokemon(self, name: str, http_client: httpx.AsyncClient) -> PokemonResponseDTO:
        pokemon_name = name.strip().lower()

        if not pokemon_name:
            raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

        pokemon_data = await self.client.get_pokemon_data(pokemon_name, http_client)

        # Extraer tipos
        types_list = [t["type"]["name"] for t in pokemon_data["types"]]

        return PokemonResponseDTO(
            name=pokemon_data["name"],
            id=pokemon_data["id"],
            weight=pokemon_data["weight"],
            height=pokemon_data["height"],
            types=types_list
        )