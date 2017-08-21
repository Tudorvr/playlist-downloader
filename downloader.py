#! /usr/bin/env python

# Downloads an playlist from youtube as mp3s
# Depends on youtube_dl, install with pip install youtube-dl
# This script is MIT licensed
# This script is not to be used for any illegal shenanigans

import youtube_dl

listurl = ""

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3
  'outtmpl': '%(title)s.mp3',    # name the file the ID of the video
  'noplaylist' : False,    # only download single song, not playlist
}

downloader = youtube_dl.YoutubeDL(options)

downloader.download([listurl])
