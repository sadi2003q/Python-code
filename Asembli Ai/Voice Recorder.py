import wave
import pyaudio

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []

try:
    print("Recording... Press Ctrl+C to stop.")
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    print("Recording stopped.")

stream.stop_stream()
stream.close()
audio.terminate()

output_filename = "new_audio.wav"
with wave.open(output_filename, "wb") as sound_file:
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))

print(f"Audio saved as {output_filename}")