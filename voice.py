import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer

class VoiceAI:

    def __init__(self, vosk_name = "vosk-model-small-en-us-0.15"):
        self.queue = queue.Queue()
        self.model = vosk_name


    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.queue.put(bytes(indata))


    def voice(self, fn):
        device_info = sd.query_devices(None, "input")
        samplerate = int(device_info["default_samplerate"])
            
        # model = Model(lang="en-us")
        # model = Model(model_name="vosk-model-en-us-0.22")
        # model = Model(model_name="vosk-model-en-us-0.42-gigaspeech")
        model = Model(model_name=self.model)

        with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=None, dtype="int16", channels=1, callback=self.callback):
            rec = KaldiRecognizer(model, samplerate)

            while True:
                data = self.queue.get()

                if rec.AcceptWaveform(data):
                    fn(rec.Result())
                else:
                    fn(rec.PartialResult())