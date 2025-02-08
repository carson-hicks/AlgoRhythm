# beat detector test
import librosa

# 1. Get the file path to an included audio example
filename = "sample_compositions/1/1.mp3" # 90 BPM, C Major

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename, sr=None)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(tempo)

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
