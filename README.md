USED CHATGPT TO WRITE THIS DOCUMENTATION !!!


Spotify Playlist Copier
This script allows you to create a new private playlist on Spotify and add all your saved tracks (from the "Liked Songs" library) to it using the Spotify Web API.

Features
Authorization: Uses OAuth2 to authenticate with Spotify.
Saved Tracks Fetching: Retrieves all saved tracks from your Spotify library.
Playlist Creation: Creates a new private playlist titled "Liked Songs Copy."
Track Addition: Adds all saved tracks to the newly created playlist in batches of 100.
Error Handling: Displays helpful error messages if issues arise during execution.
Getting Started
Follow these steps to get the script up and running.

1. Prerequisites
Python 3.6 or higher
Spotify Developer Account (Create an App)
2. Install Dependencies
Clone the repository and install required Python libraries:

bash
Copy code
git clone https://github.com/yourusername/spotify-playlist-copier.git
cd spotify-playlist-copier
pip install spotipy python-dotenv
3. Spotify Developer Credentials
To use the Spotify Web API, you need to obtain a Client ID and Client Secret by registering an app on the Spotify Developer Dashboard.

Once you have your credentials, create a .env file in the root of your project and add the following lines:

dotenv
Copy code
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
Make sure to replace your_client_id_here and your_client_secret_here with the actual credentials you obtained.

4. Running the Script
After setting up the environment, you can run the script:

bash
Copy code
python your_script_name.py
The script will:

Open a browser window for you to log in to Spotify and authorize the app.
Fetch your saved tracks.
Create a new private playlist.
Add all saved tracks to the playlist.
5. Result
Once the script finishes, you will see the following message:

rust
Copy code
Playlist 'Liked Songs Copy' successfully created!
Configuration
You can customize the script by editing the following variables in the code:

Track Batch Size: The script fetches and adds tracks in batches of 100. You can change this by modifying the LIMIT variable.
Playlist Name: Change the name of the playlist by editing the name="Liked Songs Copy" parameter in the user_playlist_create method.
Possible Extensions
Filtering Tracks: Modify the script to only add tracks with specific genres, ratings, or other criteria.
Public Playlist: To make the playlist public, change the public=False to public=True when creating the playlist.
Error Handling
If any issues occur during the script's execution, such as invalid credentials, network problems, or no liked songs, appropriate error messages will be shown in the console.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-name).
Open a Pull Request.

This project provides a simple way to manage your Spotify playlists by copying all liked songs to a new playlist. It's fully customizable, and you can extend it to suit your needs.
