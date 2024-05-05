from flask import Flask, abort, request
from tempfile import NamedTemporaryFile
import whisper
import torch

torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("base", device=DEVICE)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Whisper is running!"


@app.route('/whisper/transcribe', methods=['POST'])
def transcribe():
    if not request.files:
        abort(400)

    results = []

    for filename, handle in request.files.items():
        temp = NamedTemporaryFile()
        handle.save(temp)

        result = model.transcribe(temp.name)
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    return {'results': results}

    
@app.route('/whisper/translate', methods=['POST'])
def translate():
    if not request.files:
        abort(400)

    results = []

    for filename, handle in request.files.items():
        temp = NamedTemporaryFile()
        handle.save(temp)

        audio = whisper.load_audio(temp.name)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        _, probs = model.detect_language(mel)

        result = model.transcribe(temp.name, language=max(probs, key=probs.get), task="translate")
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    return {'results': results}
