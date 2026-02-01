import httpx
from fastapi import APIRouter

# IMPORTANTE: Aquí importamos las clases con los nombres NUEVOS que creamos antes
from services.pokemonServices import PokemonService
from DTOs.pokemonDtos import PokemonResponseDTO

# Creamos el router. El prefijo "/api" significa que la URL completa será:
# http://localhost:8000/api/pokemon/{name}
router = APIRouter(prefix="/api")

@router.get("/pokemon/{name}", response_model=PokemonResponseDTO)
async def get_pokemon(name: str):
    """
    Endpoint para obtener información de un Pokémon.
    
    Args:
        name (str): Nombre del Pokémon a buscar (ej: pikachu)
        
    Returns:
        PokemonResponseDTO: JSON con los datos del Pokémon
    """
    
    # Creamos un cliente HTTP asíncrono (se abre y se cierra automáticamente)
    async with httpx.AsyncClient() as http_client:
        # 1. Instanciamos el servicio de Pokémon
        pokemon_service = PokemonService()
        
        # 2. Llamamos al método que busca el Pokémon
        # Le pasamos el nombre que recibimos en la URL
        pokemon_response = await pokemon_service.get_pokemon(name, http_client)
        
        # 3. Devolvemos la respuesta
        return pokemon_response