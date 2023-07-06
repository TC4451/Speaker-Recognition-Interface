import sounddevice as sd
import soundfile as sf
import os
import time

# duration of recording
duration = 3
# output audio file name 
output_file = "temp.wav"

# record audio from default microphone and write it to a file
def record_audio(duration, output_file):
    # Set the desired sample rate and number of channels
    sample_rate = 44100  # 44.1kHz
    channels = 2 

    # Record audio using sounddevice
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait for recording to finish

    # Save the recorded audio to a file
    sf.write(output_file, recording, sample_rate)


# record_audio(duration, output_file)

# time.sleep(5)

# # Delete the recorded file
# os.remove(output_file)