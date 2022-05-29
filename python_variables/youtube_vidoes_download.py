from pytube import YouTube
from pytube.streams import Stream
link=input("Enter Youtube URL")
video=YouTube(link)
Stream=video.streams.get_highest_resolution()
Stream.download()
