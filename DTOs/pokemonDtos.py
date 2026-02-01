"""
=============================================================================
DTOs (DATA TRANSFER OBJECTS) - MODELOS DE DATOS
=============================================================================

Este módulo contiene los DTOs (Data Transfer Objects) utilizados para
estructurar los datos de respuesta de la API.

¿Qué es un DTO?
---------------
Un DTO es un objeto que define la estructura de los datos que se transfieren
entre capas de la aplicación o hacia/desde clientes externos.

¿Por qué usar DTOs en FastAPI?
------------------------------
1. VALIDACIÓN AUTOMÁTICA: Pydantic valida que los datos cumplan el esquema
2. DOCUMENTACIÓN: FastAPI genera docs automáticos (Swagger) basados en los DTOs
3. SERIALIZACIÓN: Convierte automáticamente objetos Python a JSON
4. TYPE HINTS: Mejora el autocompletado y detección de errores en el IDE
5. CONSISTENCIA: Garantiza que todas las respuestas tengan el mismo formato

Ejemplo de respuesta generada:
{
    "name": "pikachu",
    "id": 25,
    "weight": 60,
    "height": 4,
    "types": ["electric"]
}

Autor: [Tu nombre]
Fecha: Enero 2026
=============================================================================
"""

# BaseModel es la clase base de Pydantic para definir modelos de datos
# Proporciona validación automática, serialización y documentación
from typing import List
from pydantic import BaseModel, Field


class PokemonResponseDTO(BaseModel):
    """
    DTO para la respuesta de información de Pokémon.
    
    Este modelo define la estructura exacta de los datos que se devuelven
    cuando un usuario consulta un Pokémon por su nombre.
    
    Características:
    - Todos los campos son obligatorios (no tienen valor por defecto)
    - FastAPI valida automáticamente que los datos cumplan este esquema
    - Se genera documentación automática en Swagger UI
    
    Atributos:
        name (str): Nombre del Pokémon
        id (int): Identificador único en la Pokédex
        weight (int): Peso del Pokémon (en hectogramos)
        height (int): Altura del Pokémon (en decímetros)
        types (List[str]): Lista de tipos elementales (ej: fuego, agua)
    
    Ejemplo:
        >>> pokemon = PokemonResponseDTO(
        ...     name="charizard",
        ...     id=6,
        ...     weight=905,
        ...     height=17,
        ...     types=["fire", "flying"]
        ... )
        >>> pokemon.model_dump()  # Convierte a diccionario
        {'name': 'charizard', 'id': 6, 'weight': 905, 'height': 17, 'types': ['fire', 'flying']}
    """

    # =========================================================================
    # CAMPO: name (nombre del Pokémon)
    # =========================================================================
    # Field(...) indica que el campo es OBLIGATORIO
    name: str = Field(
        ...,  # ... significa que es un campo requerido
        description="Nombre oficial del Pokémon",
        examples=["pikachu", "bulbasaur", "mewtwo"]
    )

    # =========================================================================
    # CAMPO: id (Identificador de Pokédex)
    # =========================================================================
    # int porque el ID siempre es un número entero
    id: int = Field(
        ...,
        description="Número identificador en la Pokédex Nacional",
        examples=[25, 1, 150]
    )

    # =========================================================================
    # CAMPO: weight (Peso)
    # =========================================================================
    # Según la PokeAPI, el peso viene en hectogramos
    weight: int = Field(
        ...,
        description="Peso del Pokémon",
        examples=[60, 69, 1220]
    )

    # =========================================================================
    # CAMPO: height (Altura)
    # =========================================================================
    # Según la PokeAPI, la altura viene en decímetros
    height: int = Field(
        ...,
        description="Altura del Pokémon",
        examples=[4, 7, 20]
    )

    # =========================================================================
    # CAMPO: types (Tipos elementales)
    # =========================================================================
    # Es una lista de strings (List[str]) porque un Pokémon puede tener uno o dos tipos
    types: List[str] = Field(
        ...,
        description="Lista de tipos a los que pertenece el Pokémon",
        examples=[["electric"], ["grass", "poison"], ["fire", "flying"]]
    )

    # =========================================================================
    # CONFIGURACIÓN DEL MODELO (opcional pero útil)
    # =========================================================================
    class Config:
        """
        Configuración adicional del modelo Pydantic.
        
        json_schema_extra: Permite agregar ejemplos completos que aparecen
                           en la documentación de Swagger UI.
        """
        json_schema_extra = {
            "example": {
                "name": "pikachu",
                "id": 25,
                "weight": 60,
                "height": 4,
                "types": ["electric"]
            }
        }