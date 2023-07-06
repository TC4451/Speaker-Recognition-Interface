import torchaudio
from speechbrain.pretrained import SpeakerRecognition

# perform speaker verification
verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
score, prediction = verification.verify_files("tests/samples/ASR/spk1_snt1.wav", "tests/samples/ASR/spk2_snt1.wav") # Different Speakers
score, prediction = verification.verify_files("tests/samples/ASR/spk1_snt1.wav", "tests/samples/ASR/spk1_snt2.wav") # Same Speaker

# for each file in speaker_voice_sample, compare it. If the score is 1, print name, if the score is 0, skip.
# if all is 0, then print "unrecognizable"