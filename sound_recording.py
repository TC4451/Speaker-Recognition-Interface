import sounddevice as sd
import soundfile as sf
import os
import time
import torch

# duration of recording
duration = 3
# output audio file name 
output_file = "temp.wav"
# defined sample rate
sample_rate = 16000
# defined number of channels
channels = 2 

# record audio from default microphone and write it to a file
def record_sample(duration, output_file):
    # Record audio using sounddevice
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait for recording to finish

    # Save the recorded audio to a file
    sf.write(output_file, recording, sample_rate)

# record audio and convert it to a tensor
def audio_to_tensor(duration):
    # Record audio using sounddevice
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait for recording to finish

    audio_tensor = torch.from_numpy(recording)

    return audio_tensor


# record_audio(duration, output_file)

# time.sleep(5)

# # Delete the recorded file
# os.remove(output_file)