import ffmpeg

filename = ""
startframe=32
endframe=42
input_file = ffmpeg.input('eng100\.mp4')

output_file = ffmpeg.output(input_file.trim(start_frame=30*23.976023976023978, end_frame=35*23.976023976023978), 'aoutput.mp4')
ffmpeg.run(output_file)
print("Video timmed")