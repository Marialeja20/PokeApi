from fastapi import FastAPI
# Importamos el router con un nombre coherente
from controllers.pokemonController import router as pokemon_router

app = FastAPI(
    title="Pokémon API",
    description="""
    ## API de Pokédex 🎮
    Consulta datos oficiales de Pokémon usando PokeAPI.
    """,
    version="1.0.0",
    contact={
        "name": "Mary",
        "email": "mary@example.com"
    }
)

@app.get("/", tags=["General"])
def home():
    return {
        "message": "Welcome to the Pokémon API",
        "docs": "/docs",
        "version": "1.0.0"
    }

# Registro del router de Pokémon
app.include_router(pokemon_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)