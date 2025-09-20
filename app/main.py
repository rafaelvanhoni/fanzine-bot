from app.services.discogs_service import DiscogsService
from app.core.models.artist import Artist
import json

if __name__ == "__main__":
    discogs = DiscogsService()
    data = discogs.fetch_data("Ramones","artist")

    if data:
        artistas = []
        for item in data["results"]:
            print(f"→ Criando artista: {item['title']} (id={item['id']})")
            artista = Artist.from_dict(item)
            print("🎨 Objeto Artist criado:", artista)
            
            artistas.append(artista)

    for artista in artistas:
        print(repr(artista))