# this file manages both sample audio recording and real-time sound-to-tensor conversion

import sounddevice as sd
import soundfile as sf
import threading
import client_sb
import numpy as np
import time

# duration of recording
duration = 2
# output audio file name 
output_file = "temp.wav"
# defined sample rate
sample_rate = 16000
# defined number of channels
channels = 1 

# record audio from default microphone and send it to linux machine
def record_sample(duration, output_file):
    def recording_thread():
        # Record audio using sounddevice
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float64')
        sd.wait()  # Wait for recording to finish

        # # Save the recorded audio to a file
        # sf.write(output_file, recording, sample_rate)
        # from scipy.io import wavfile
        # wavfile.write("output.wav", sample_rate, recording)
        client_sb.send_nparray_no_response(recording)
        print(recording)
        print(recording.shape)
        client_sb.send_string(output_file)

    threading.Thread(target=recording_thread).start()

# record audio and convert it to a tensor
def audio_to_numpy(duration):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait for recording to finish
    return recording

# connect to server and pass the 1 sec recording for processing
# return: name of the speaker
def verify_speaker(audio_np):
    name = client_sb.send_nparray_for_identification(audio_np)
    return name

# connet to server to load sample audios into instance variables to start recognition
def load_samples():
    client_sb.send_string('load_samples')
    


# --------------------testing-------------------------#

# # test whether the numpy arrays are the same on linux and local machine
# def nparray_sync_testing():
#     recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float64')
#     sd.wait()
#     np.save('./testing_stuff/numpy_sync_testing.npy', recording)


# nparray_sync_testing()
# # nparray_sync_testing
# arr = np.load('./testing_stuff/numpy_sync_testing.npy')
# print(arr)
# time.sleep(1)
# client_sb.send_nparray_no_response(arr)
# client_sb.send_string('server_numpy_sync_testing.npy')


# record_audio(duration, output_file)

# time.sleep(5)

# # Delete the recorded file
# os.remove(output_file)