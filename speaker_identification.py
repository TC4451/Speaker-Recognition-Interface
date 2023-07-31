import torchaudio
from speechbrain.pretrained import SpeakerRecognition
import sound_recording
import os
import torch

# perform speaker verification
verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
# audio_tensor = sound_recording.audio_to_tensor()
# audio_tensor = verification.audio_normalizer(audio_tensor)

# sample_paths = os.listdir("./speaker_voice_sample")
# for file_path in sample_paths:
#     sample_audio = verification.load_audio(file_path)
#     batch_x = audio_tensor.unsqueeze(0)
#     batch_y = audio_tensor.unsqueeze(0)
#     score, decision = verification.verify_batch(batch_x, batch_y)
#     print(score[0])

def identify_speaker():
    # voice sample directory
    sample_dir = './speaker_voice_sample/'
    # list all samples in directory
    sample_list = os.listdir(sample_dir)
    recording = sound_recording.audio_to_tensor(1)
    scores = {}
    recording_unsqueeze = recording.unsqueeze(0)
    for sample in sample_list:
        sample_audio = verification.load_audio(sample_dir + sample)
        sample_audio_unsqueeze = sample_audio.unsqueeze(0)
        score[sample] = verification.verify_batch(recording_unsqueeze, sample_audio_unsqueeze)[0]
    return max(score, key = score.get())
    

score, prediction = verification.verify_files("./speaker_voice_sample/zilin.wav", "./speaker_voice_sample/zilin.wav") # Different Speakers
# score, prediction = verification.verify_files("tests/samples/ASR/spk1_snt1.wav", "tests/samples/ASR/spk1_snt2.wav") # Same Speaker
print(score)
print(prediction)
