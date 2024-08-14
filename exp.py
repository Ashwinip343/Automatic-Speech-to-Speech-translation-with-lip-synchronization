from pytube import YouTube
from PIL import Image
import ffmpeg
from pydub import AudioSegment 
import os 

directory="/Users/ashwinipatil/Developer/ytb"

# link="https://youtu.be/UUheH1seQuE?si=ZSCcqxnGXbs-i7Zq"
# link="https://youtu.be/WLQ6HyFbfKU?si=I3rKIp0M_EZ8qhv1"
# link="https://youtu.be/zUEJwekzz-g?si=et7DNPfSkX43zMXe"
# link="https://youtu.be/9L8VQFRQDWc?si=MWLhdLNzUumKxkgg"

# link="https://youtu.be/zUEJwekzz-g?si=JGiiYMpaE6zo-JE2"
# link="https://youtu.be/B3GWnhwIDIw?si=qRb3h7xubOJo_uLD"
# link="https://youtu.be/Cz24meZACsY?si=0rUJHngl9hJUqmgF"
# link="https://www.youtube.com/live/IVF_ms3G2O8?si=MQWquJiEzMbLlbBh"
# link="https://youtu.be/V3l-WUFRpmg?si=f0S3H8HmlxNI3ei3"
# link="https://youtu.be/Ff1vqV9_knQ?si=9RrlLHOGTV8Fwizq"
# link="https://youtu.be/cFhONVldyE0?si=MC87ViYAIzNjrfv_"
link="https://youtu.be/V92Mi54hQ5o?si=2iUEzLj060PAN5K7"
# link="https://youtu.be/ZVpkFb9-fts?si=6xFBqHCWJDLOCGzc"
name="deep_hehe_voice"
ytb=YouTube(link)
stream = ytb.streams.get_by_itag(22)
count=100
stream.download(output_path=directory,filename=f"{name}{count}.mp4")
print(ytb.title)

input_file = ffmpeg.input(f'{directory}/{name}{count}.mp4')
input_file.output(f"{name}{count}.mp3", acodec='mp3').run()
sound = AudioSegment.from_mp3(f'{name}{count}.mp3') 
sound.export(f"{name}{count}.wav", format="wav") 





# try:
#     rmaudio=os.remove(f'{directory}/{name}{count}.mp3')
#     rmvideo=os.remove(f'{directory}/{name}{count}.mp4')
#     print(f"Removed files:{rmaudio},{rmvideo} ")
    
# except OSError as e: 
#     print(f"Error deleting : {e}")
    

    # \Users|pymld\Downloads\Video>ffmpeg -i input.mkv -c copy -map 0 -segment_time 00:10:00 -f segment -res et_timestamps 1 output%03d. mkv