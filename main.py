from pytube import YouTube

# paste the YouTube video URL you want to download here
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# create a YouTube object
yt = YouTube(video_url)

# get the first stream with the highest resolution
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

# download the video to the current directory
stream.download()
