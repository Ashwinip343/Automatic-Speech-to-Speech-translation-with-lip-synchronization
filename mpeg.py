import pydub

input_file = "/Users/ashwinipatil/Developer/ytb/ash.mpeg"  # Replace with your actual file path
output_file = "ash.mp3"

try:
    # Open MPEG audio file (pydub automatically detects format)
    sound = pydub.AudioSegment.from_file(input_file)

    # Optionally adjust audio parameters (e.g., bitrate)
    # sound = sound.set_bitrate(bitrate=192000)  # Example: Set bitrate to 192 kbps

    # Export to MP3
    sound.export(output_file, format="mp3")
    print(f"Successfully converted {input_file} to {output_file}")
except Exception as e:
    print(f"Error during conversion: {e}")
