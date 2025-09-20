from app.core.models.artist import Artist

def test_artist_str():
    artist = Artist(
        id=135478,
        type="artist",
        user_data={},
        master_id=None,
        master_url=None,
        uri="/artist/135478-Ramones",
        title="Ramones",
        thumb="https://link/thumb.jpg",
        cover_image="https://link/cover.jpg",
        resource_url="https://api.discogs.com/artists/135478"
    )
    assert str(artist) == "Ramones, id: 135478"    