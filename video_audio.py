# from pytube import YouTube
from PIL import Image
import ffmpeg
from pydub import AudioSegment 
import os 


directory="/Users/ashwinipatil/Developer/AIMLDS/ytb/new_modi_trimmed.mp4"
name="a_modi_audio"

input_file = ffmpeg.input(directory)
input_file.output(f"{name}.mp3", acodec='mp3').run()
sound = AudioSegment.from_mp3(f'{name}.mp3') 
sound.export(f"{name}.wav", format="wav") 