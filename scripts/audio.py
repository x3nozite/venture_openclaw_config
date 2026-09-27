import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
import wave
import requests
from datetime import date

import os
from dotenv import load_dotenv

fs = 16000
channels = 1
audio_data = []
model = WhisperModel("small", compute_type="float32", device="cpu")

load_dotenv("./.env")
token = os.environ["OPENCLAW_GATEWAY_TOKEN"]


def callback(indata, frames, time, status):
    audio_data.append(indata.copy())


input_stream = sd.InputStream(
    samplerate=fs, channels=channels, dtype="int16", callback=callback)
with input_stream:
    input("Press enter to stop\n")

print("finished")


audio = np.concatenate(audio_data, axis=0)
audio = audio.flatten().astype((np.float32)) / 32768.0

with wave.open("debug.wav", 'wb') as f:
    f.setnchannels(channels)
    f.setsampwidth(2)
    f.setframerate(fs)
    f.writeframes((audio * 32768).astype(np.int16).tobytes())

segments, info = model.transcribe(audio, beam_size=5, language="en")

text = " ".join(segment.text for segment in segments)
print(text)
print(info.language, info.language_probability)


def send_to_openclaw(text, token, url="http://127.0.0.1:18789/v1/chat/completions"):
    today = date.today().isoformat()
    resp = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openclaw/venture-creation-agent",
            "user": f"x3no-{today}",
            "messages": [{"role": "user", "content": text}]
        }
    )

    return resp.json()["choices"][0]["message"]["content"]


reply = send_to_openclaw(text, token)
print("Openclaw: ", reply)
