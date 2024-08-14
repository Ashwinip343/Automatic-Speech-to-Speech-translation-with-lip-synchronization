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
# link="https://youtu.be/idtZ_DsPWT8?si=O30kRH4NUf9HSzTD"
link="https://youtu.be/fetkfl5hN_c?si=oh5I7DwsCqDcHCHY"

# link="https://youtu.be/ZVpkFb9-fts?si=6xFBqHCWJDLOCGzc"
name="deepika_"
ytb=YouTube(link)
stream = ytb.streams.get_by_itag(22)
count=100
stream.download(output_path=directory,filename=f"{name}{count}.mp4")
