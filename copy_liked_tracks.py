import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://:8888/callback'

# Авторизация
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private user-library-read"
))


liked_tracks = []
results = sp.current_user_saved_tracks(limit=100)
while results:
    for item in results['items']:
        liked_tracks.append(item['track']['id'])
    results = sp.next(results) if results['next'] else None

user_id = sp.current_user()['id']
new_playlist = sp.user_playlist_create(user=user_id, name="Liked Songs Copy", public=False)

# Добавление треков в плейлист
for i in range(0, len(liked_tracks), 100):
    sp.playlist_add_items(new_playlist['id'], liked_tracks[i:i+100])

print(f"Плейлист 'Liked Songs Copy' создан!")
