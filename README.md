# Spotify Library Fixer

This script is a quick hack to make deal with the fact that Spotify only 
allows 10000 tracks in a given library. The "fix" is to move the items from
your library to a playlist. 

## Usage

You'll need to register with Spotify to get credentials so you can call their
API directly. Do this at https://developer.spotify.com/. Once you're signed up
and logged in, create a new app to get a client ID. It doesn't matter what you
call it. Be sure to set up a callback URL using a URL that you don't mind
getting passed the auth token that Spotify generates. You don't actually need
a server for this -- Spotify will simply redirect the request with the auth
token as a request parameter.

Once you have the client ID and secret specified when you created your app, set
the following environment variables:

```sh
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

Once those are set, you can initialize the Python environment: 

```sh
pipenv shell && pipenv install
```

Finally, run the script with your Spotify username and the name you'd like to
use for the playlist (use quotes if you are using more than one word). E.g.,

```sh
./fixer.py tlockney "Library 1"
```