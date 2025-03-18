

# Spotify Playlist Copier

This script allows you to create a new private playlist on Spotify and add all your saved tracks (from the "Liked Songs" library) to it using the Spotify Web API.

---

## **Features**

- **Authorization:** Uses OAuth2 to authenticate with Spotify.
- **Saved Tracks Fetching:** Retrieves all saved tracks from your Spotify library.
- **Playlist Creation:** Creates a new private playlist titled "Liked Songs Copy."
- **Track Addition:** Adds all saved tracks to the newly created playlist in batches of 100.
- **Error Handling:** Displays helpful error messages if issues arise during execution.

---

## **Getting Started**

Follow these steps to get the script up and running.

### 1. **Prerequisites**

- [Python](https://www.python.org/downloads/) 3.6 or higher
- Spotify Developer Account ([Create an App](https://developer.spotify.com/dashboard/applications))

### 2. **Install Dependencies**

Clone the repository and install the required Python libraries:

```bash
git clone https://github.com/yourusername/spotify-playlist-copier.git
cd spotify-playlist-copier
pip install spotipy python-dotenv
