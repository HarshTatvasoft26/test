import yt_dlp
import os

# URL of the YouTube playlist
playlist_url = 'https://youtube.com/playlist?list=PL78RhpUUKSwfeSOOwfE9x6l5jTjn5LbY3&feature=shared'

# Folder to save the downloaded videos
download_folder = 'downloaded_videos'

# Create the folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Options for yt-dlp
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
}

# Download playlist using yt-dlp
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print(f"All available videos have been downloaded to the folder: {download_folder}")