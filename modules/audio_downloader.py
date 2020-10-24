from __future__ import unicode_literals
import youtube_dl as yt

def download_sound_file(sound_link, source='youtube'):
    """
    Downloads the audio file of the video
    """
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with yt.YoutubeDL(ydl_opts) as ydl:
    ydl.download([sound_link])

    return True
