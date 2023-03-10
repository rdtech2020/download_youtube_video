# Download YouTube Videos using Python

This project demonstrates how to download YouTube videos using Python. The pytube library is used in this project, which provides a simple way to access and download YouTube videos.

### Prerequisites
Before running the code, you will need to install the `pytube` library. You can install `pytube` using `pip`:
```py
pip install pytube
```

### How to use the code
To use the code, simply paste the URL of the YouTube video you want to download into the `video_url` variable in the code. Then run the code using Python. The video will be downloaded to the current directory.
```py
from pytube import YouTube

# paste the YouTube video URL you want to download here
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# create a YouTube object
yt = YouTube(video_url)

# get the first stream with the highest resolution
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

# download the video to the current directory
stream.download()
```
### Project structure
The project contains the following file:
* `main.py`: The main Python script that contains the code for downloading YouTube videos.
* `README.md`: This file, which provides information about the project.
* `LICENSE`: The license file for the project.

### Contributing
If you find any issues or have any suggestions for the project, feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the `LICENSE.md` file for details.
