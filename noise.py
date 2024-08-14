from scipy.io import wavfile
import noisereduce as nr

# load data
rate, data = wavfile.read("new_modiaudio0.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
print("Done")
wavfile.write("new_modi_reduced_noise.wav", rate, reduced_noise)
print("Done")
