import lyricsgenius
from Token import client_access_token
genius = lyricsgenius.Genius(client_access_token)

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

print("The Song Writer is: " + searchWriter("415", "Anhedonia"))
