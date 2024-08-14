import os 
# import 
import ffmpeg

import subprocess

def trim_video(input_file, start_time, end_time, output_file):

  command = [
      "ffmpeg",
      "-y",  # Overwrite output file if it exists
      "-i", input_file,  # Input video file
      "-ss", f"{start_time}",  # Start time in seconds (formatted string)
      "-to", f"{end_time }",  # Duration (end time - start time)
      output_file,  # Output video file
  ]
  # Execute the ffmpeg command using subprocess
  subprocess.run(command)

# Example usage
input_file = "deep_hehe_voice100.mp4"
start_time = 224 # Start at 10 seconds
end_time = 244 # End at 20 seconds
output_file = "hehe_trimmed.mp4"

trim_video(input_file, start_time, end_time, output_file)

print("Video trimmed successfully!")
