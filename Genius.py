import lyricsgenius
from Token import client_access_token
genius = lyricsgenius.Genius(client_access_token)

def getArtistID(artist):
    artist_id = genius.find_artist_id(artist)
    return artist_id["id"]


def searchSong(title, artist):
    song = genius.search_song(title, artist)
    return song


def searchWriter(title, artist):
    song = searchSong(title, artist)
    if song == None:
        return None
    else:
        try:
            writer = song.writer_artists[0]["name"]
            return writer
        except IndexError:
            return None
print(getArtistID("Khalid"))
print("The Song Writer is: " + searchWriter("Khalid", "8TEEN"))
"""
search_results = genius.search_genius("Joel Little")["hits"]
for item in search_results:
    result = item["result"]
    print(result)
    print(result["full_title"])

"""


search_results = genius.search_artist(artist_name="Joel Little", include_features=True)
print(search_results)