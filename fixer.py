#!/usr/bin/env python

import sys

import spotipy
import spotipy.util as util

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} [username] [playlist name]")
    sys.exit()
else:
    username = sys.argv[1]
    playlist_name = sys.argv[2]

scope="""
    user-library-read
    user-library-modify
    playlist-modify-public
"""
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print(f"Can't get token for {username}")
    sys.exit()

user_id = sp.current_user()['id']

lists = sp.user_playlists(user_id)['items']
playlists = {item['name']:item for item in lists}

if playlist_name in playlists.keys():
    print(f"Playlist {playlist_name} already exists")
    playlist_id = playlists[playlist_name]['id']
else:
    print(f"Creating list {playlist_name}")
    res = sp.user_playlist_create(user_id, "Library 1", True)
    playlist_id = res['id']

try:
    track_results = sp.current_user_saved_tracks(50)

    while track_results:
        tracks = [item['track'] for item in track_results['items']]
        track_ids = [track['id'] for track in tracks]
        sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)
        sp.current_user_saved_tracks_delete(track_ids)
        track_results = sp.next(track_results)
except Exception as e:
    print(f"No tracks found or error encountered: {e}")

print("\nAll done!")