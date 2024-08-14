from pytube import YouTube
import ffmpeg
from pydub import AudioSegment
import tempfile
import os

link = "https://youtu.be/dSHJYyRViIU?si=brQdivK9akYzwjps"
ytb = YouTube(link)
stream = ytb.streams.get_by_itag(22)
count = 10

# Use temporary file for MP3 conversion

with tempfile.NamedTemporaryFile(suffix=".mp4", delete=True) as temp_file:
    stream.download(output_path="/Users/ashwinipatil/Developer/ytb", filename=temp_file.name)
    
    input_file = ffmpeg.input("/Users/ashwinipatil/Developer/ytb/"+temp_file.name)
    input_file.output(temp_file.name, acodec='mp3').run()

    # Process the audio from the temporary MP3 file (e.g., convert to WAV)
    sound = AudioSegment.from_mp3(temp_file.name)
    sound.export(f"audio{count}.wav", format="wav")

# Delete the temporary MP3 file after processing
os.remove(temp_file.name)
print(ytb.title)
