Documentation for the Code  (used chatGPT to write documentation) !!!!
Description
This code allows you to create a new private playlist on Spotify and add all your saved tracks (from the "Liked Songs" library) to it. It uses the spotipy library to interact with the Spotify API and OAuth2 for authorization. The code supports authorization, playlist creation, and track addition.

Steps for Usage
1. Setting Up the Environment
Before running the code, you need to complete several preparation steps:

1.1 Installing Dependencies
To run this code, you need to install the spotipy and python-dotenv libraries to handle API requests and securely load configuration data.

bash
Copy code
pip install spotipy python-dotenv
1.2 Obtaining Authorization Credentials
To access the Spotify API, you must register an application in the Spotify Developer Dashboard. After registering, you will receive:

Client ID
Client Secret
Redirect URI
Save these values for use later.

1.3 Creating a Configuration File
For security and convenience in loading configuration, it's best to use a .env file. This file should contain your Spotify API credentials.

Create a .env file in the root of your project directory and add the following lines:

makefile
Copy code
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
Replace your_client_id_here and your_client_secret_here with the actual values from the Spotify Developer Dashboard.

2. Running the Code
Once you have set up the environment and the configuration file, you can run the code. Simply execute the script:

bash
Copy code
python your_script_name.py
3. What the Code Does
Authorization: The code uses OAuth2 for authorization and access to your Spotify account. On the first run, a browser window will open for you to log in to your account and grant the necessary permissions.

Fetching Saved Tracks: The code fetches all your saved tracks from your Spotify library (first 100, then the next batch if there are more).

Creating a Playlist: After gathering all the tracks, the code creates a new private playlist named "Liked Songs Copy."

Adding Tracks to the Playlist: All the collected tracks are added to the created playlist. Tracks are added in batches of 100 to avoid exceeding the API request limit.

Result: Once the script finishes, the following message will be displayed:

rust
Copy code
Playlist 'Liked Songs Copy' successfully created!
4. Errors and Handling
If any errors occur during execution (e.g., authorization issues, network problems), the code will output an error message to the console. If there are no saved tracks, the following message will be displayed:

perl
Copy code
You have no liked songs.
5. Configuration
Track Batch Size: The code fetches and adds tracks in batches of 100. This is an API limitation imposed by Spotify. You can change this batch size by modifying the LIMIT variable in the code.

Reusing the Code: You can use this code to create other playlists by changing the playlist name in the line:

python
Copy code
new_playlist = sp.user_playlist_create(user=user_id, name="Liked Songs Copy", public=False)
Simply replace "Liked Songs Copy" with any other name you prefer.

6. Possible Extensions
Filtering Tracks: You can modify the code to only add certain tracks (e.g., only favorites or tracks of specific genres).

Creating Public Playlists: To create a public playlist, just change the public=False to public=True when creating the playlist.

Conclusion
This code automates the process of copying saved tracks from your Spotify library into a new private playlist. It can be used to efficiently manage your music collection and transfer your favorite tracks into a new playlist for future use.
