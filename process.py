from pytube import YouTube
from PIL import Image
import ffmpeg
from pydub import AudioSegment 
import os 

directory="/Users/ashwinipatil/Developer/ytb"
link="https://youtu.be/LlsAx-TaQw4?si=GGXKQvdUu9LZWpF9"
ytb=YouTube(link)
stream = ytb.streams.get_by_itag(22)
count=100
stream.download(output_path=directory,filename=f"modi.mp4")
print(ytb.title)
input_file = ffmpeg.input(f'{directory}/modi.mp4')
input_file.output(f"audio.mp3", acodec='mp3').run()
sound = AudioSegment.from_mp3(f'audio.mp3') 
sound.export(f"modi.wav", format="wav") 
# try:
    # rmaudio=os.remove(f'{directory}/audio{count}.mp3')
    # rmvideo=os.remove(f'{directory}/modi_{count}.mp4')
    # print(f"Removed files:{rmaudio},{rmvideo} ")
    
# except OSError as e: 
    # print(f"Error deleting : {e}")
    

    # \Users|pymld\Downloads\Video>ffmpeg -i input.mkv -c copy -map 0 -segment_time 00:10:00 -f segment -res et_timestamps 1 output%03d. mkv