import os
from pydub import AudioSegment

# Path to your WAV file
name="deepika"
count=100
# wav_file = f"/Users/ashwinipatil/Developer/ytb/{name}{count}.wav"
wav_file="deepika_30_22.wav"

# Chunk duration in milliseconds (10 seconds)
chunk_length = 10 * 1000  # 10 seconds * 1000 milliseconds/second
sound = AudioSegment.from_wav(wav_file)

# Calculate total number of chunks
total_chunks = len(sound)//chunk_length

# Generate chunks and save them
for i in range(total_chunks):
  start_time = i*chunk_length
  end_time = start_time + chunk_length
  chunk = sound[start_time:end_time]

  # Generate filename with zero-padded numbering
  # output_filename = f"{name}audio{i}.wav"
  output_filename = f"deepika_10_{i}.wav"
  chunk.export(output_filename, format="wav")
