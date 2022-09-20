from pytube import YouTube
import os

yt = YouTube(str(input("Enter the Youtube video URL : ")))

audio = yt.streams.filter(only_audio=True).first()

print("Enter Save Location [ Blank for Local Directory ] : ")
loc = str(input(">>  ")) or '.'

out_file = audio.download(output_path=loc)

base,_ = os.path.splitext(out_file)
new_audio = base+'.mp3'
os.rename(out_file, new_audio)

print(yt.title + "has been successfully downloaded . ")