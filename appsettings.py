import os
from dotenv import load_dotenv

load_dotenv()

class AppSettings:
    """Configuración centralizada para la Pokémon API."""
    
    # URL Base de PokeAPI
    POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
    
    # Tiempo de espera para peticiones externas
    TIMEOUT_SECONDS = 10.0