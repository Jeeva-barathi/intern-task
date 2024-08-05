import pyaudio
import wave
FORMAT = pyaudio.paInt16 
CHANNELS = 1  
RATE = 44100  
CHUNK = 1024  
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
print("Recording...")
frames = []
for _ in range(0, int(RATE / CHUNK * 5)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Finished recording.")
stream.stop_stream()
stream.close()
audio.terminate()
output_file = "recorded_audio.wav"
wave_file = wave.open(output_file, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()

print(f"Audio recorded and saved to {output_file}")