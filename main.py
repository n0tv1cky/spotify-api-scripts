import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your credentials
CLIENT_ID = '2fd811ef23d04ac486479122098f8b1e'  # Replace with your Client ID
# Replace with your Client Secret
CLIENT_SECRET = '740a2c24f8eb4b16b686a3967a2e93e1'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-library-modify'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))


songs = [
    {"name": "Supersonic", "artist": "Baauer"},
    {"name": "Muay Thai", "artist": "Uma"},
    {"name": "J0YR1D3", "artist": "BABii"},
    {"name": "Still Riding", "artist": "Barry Can’t Swim"},
    {"name": "Bobby", "artist": "Nick Leng"},
    {"name": "S.N.C", "artist": "DARKSIDE"},
    {"name": "UMPA", "artist": "Fcukers"},
    {"name": "Mothers", "artist": "Fcukers"},
    {"name": "Talk", "artist": "Selena Gomez"}
]


def fetch_track_ids(songs):
    """Fetch track IDs from Spotify based on song name and artist."""
    track_ids = []
    for song in songs:
        query = f"{song['name']} artist:{song['artist']}"
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track_id = results['tracks']['items'][0]['id']
            track_ids.append(track_id)
            print(
                f"Found: {song['name']} by {song['artist']} (ID: {track_id})")
        else:
            print(f"Could not find: {song['name']} by {song['artist']}")
    return track_ids


def add_songs_to_liked(tracks):
    """Add tracks to Spotify liked songs."""
    sp.current_user_saved_tracks_add(tracks)
    print("Songs added successfully!")


# Fetch track IDs
track_ids = fetch_track_ids(songs)

# Add fetched tracks to liked songs
if track_ids:
    add_songs_to_liked(track_ids)
else:
    print("No valid tracks found to add.")
