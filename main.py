"""
This script takes an m3u file (a music playlist) and converts it into a txt file with song artist and title.
Original purpose was to create Spotify playlists from m3u playlists via a webapp like: https://soundiiz.com/tutorial/import-text-to-spotify.
You'll need to enter set variables for m3u file, txt file, and music directory at the bottom.
You'll also need to edit the RegEx on line 45 to match your own m3u directory info.
"""

import re
import os
import eyed3


def get_info(name):
    """
    Gets song info (artist + title) from song filename.

    args:
        name (str): song filename

    returns:
        str
    """

    for root, dirs, files in os.walk(music_dir):
        if name in files:
            audiofile = eyed3.load(os.path.join(root, name))
            artist = audiofile.tag.artist
            song = audiofile.tag.title
            song_info = artist + ' - ' + song
            return song_info


def main(m3u_file, output_txt):
    
    playlist = m3u_file

    output_txt = output_txt

    for x in playlist:
        # get playlist line
        playlist_line = x

        # get song filename
        try:
            song_filename = re.search('3433-3438\/Music\/([^\n]+\.mp3)', playlist_line).group(1)
        except:
            continue

        # search for song_filename in 'Music'
        song_info = get_info(song_filename)

        # write line to .txt file
        output_txt.write(song_info + '\n')


    playlist.close()
    output_txt.close()

if __name__ == "__main__":
    m3u_file = open('directory\to\file.m3u', 'r', encoding = 'utf-8')
    output_txt = open('directory\to\file.txt', 'a', encoding = 'utf-8')
    music_dir = r''
    main(m3u_file, output_txt)
