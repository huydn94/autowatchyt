from pytube import YouTube 

video = "https://www.youtube.com/watch?v=XSQT9RBKoCs" 
yt = YouTube(video)
video_length = yt.length
print ( video_length)