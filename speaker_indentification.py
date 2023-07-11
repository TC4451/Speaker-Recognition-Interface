import torchaudio
from speechbrain.pretrained import SpeakerRecognition
# import sound_recording
# import os

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


score, prediction = verification.verify_files("./speaker_voice_sample/zilin.wav", "./speaker_voice_sample/zilin2.wav") # Different Speakers
# score, prediction = verification.verify_files("tests/samples/ASR/spk1_snt1.wav", "tests/samples/ASR/spk1_snt2.wav") # Same Speaker
print(score)
print(prediction)
